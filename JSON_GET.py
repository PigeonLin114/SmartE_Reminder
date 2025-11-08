import requests
import json


url = "https://xqh5.17wanxiao.com/smartWaterAndElectricityService/SWAEServlet"

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-type": "application/x-www-form-urlencoded",
    "content-length":"183",
    "origin": "https://xqh5.17wanxiao.com",
    "priority": "u=1, i",
    "referer": "https://xqh5.17wanxiao.com/userwaterelecmini/index.html",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

cookies = {
    "acw_tc": "",
    "SERVERID": "",


}

# 在这里填请求体
data_raw = ""


response = requests.post(
    url=url,
    headers=headers,
    cookies=cookies,
    # 使用这个或下面的 data_raw
    data=data_raw,  # 使用这个确保与 curl 完全一致
    timeout=10
)



data2 = json.loads(response.text)

formatted_data = json.dumps(data2, indent=4, ensure_ascii=False)

data=data2 #这里的data与上面的data没关系了

try:
    # 解析外层的JSON
    outer_json = data

    # 解析body字段中的内层JSON字符串
    inner_json = json.loads(outer_json["body"])

    # 提取detaillist中的odd值
    if "detaillist" in inner_json and len(inner_json["detaillist"]) > 0:
        odd_value = inner_json["detaillist"][0]["odd"]
        print(f"提取到的odd值为: {odd_value}")
    else:
        print("未找到detaillist或detaillist为空")

except json.JSONDecodeError as e:
    print(f"JSON解析错误: {e}")
except KeyError as e:
    print(f"键错误: 未找到字段 {e}")
except Exception as e:
    print(f"其他错误: {e}")

















