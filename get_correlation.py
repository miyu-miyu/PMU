import pandas as pd
FILE_PATH = "./cpu_stress_qos_metrics.csv"
OUT_PUT_PATH = "./cpu_stress_correlations_ascend.csv"

def get_correlation(input_path, out_put_path, reverse):
    df = pd.read_csv(input_path)
    # 输出所有列名: df.columns
    # 输出指定列名的列:df[col_name]
    # df.columns.to_list() 
    Indices = df.columns.to_list()[1:] # index (column names) list
    # qos series
    X = df["qos"]
    correlation = {}
    for index in Indices:
        correlation[index] = X.corr(df[index], method="pearson")
    sorted_correlation = sorted(correlation.items(), key=lambda x: x[1], reverse=reverse)
    df_correlation = pd.DataFrame(sorted_correlation,columns=["PMU", "correlation"])
    df_correlation.to_csv(out_put_path, index=False)
    return df_correlation

if __name__ == "__main__":
    get_correlation(FILE_PATH, OUT_PUT_PATH,False)
