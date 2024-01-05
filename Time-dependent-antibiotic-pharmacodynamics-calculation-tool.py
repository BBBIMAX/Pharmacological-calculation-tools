import pandas as pd

def calculate_percentage_above_mic(df, mic_threshold, percentage_threshold):
    # 创建一个新列，表示每个时刻点浓度是否大于MIC
    df['above_mic'] = df['C'] > mic_threshold

    # 统计每个患者在一次循环内C大于MIC的次数
    patient_counts = df.groupby(['repl', 'id'])['above_mic'].sum()

    # 统计每个患者在一次循环内的总记录次数
    total_counts = df.groupby(['repl', 'id'])['above_mic'].count()

    # 计算达标比例
    percentage_above_mic = patient_counts / total_counts

    # 判断是否达标
    is_above_threshold = percentage_above_mic > percentage_threshold

    # 统计在100次循环中达标的比例
    overall_percentage = is_above_threshold.groupby('id').mean()

    return overall_percentage

def main():
    # 读取CSV文件
    file_path = 'C:\\DATA.csv'  # 替换成你的CSV文件路径
    df = pd.read_csv(file_path)

    # 设置MIC阈值和达标比例阈值
    mic_threshold = 8
    percentage_threshold = 0.4

    # 计算达标比例
    overall_percentage = calculate_percentage_above_mic(df, mic_threshold, percentage_threshold)

    # 输出结果
    print("达标比例:")
    print(overall_percentage)

if __name__ == "__main__":
    main()
