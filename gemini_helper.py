from openai import OpenAI

google_gemini_api_key = "AIzaSyBJH5dxiaJmC6273xswPKX1AU-s1Nx0nyo"

model = OpenAI(
    api_key=google_gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def my_google_llm(myprompt):
    mymsg = [
        {
            "role": "system",
            "content": "You are AI assistant, only works is to generate cold email with no subject"
        },
        {
            "role": "user",
            "content": myprompt
        }
    ]

    output = model.chat.completions.create(
        messages=mymsg,
        model="gemini-1.5-flash"
    )

    return output.choices[0].message.content
