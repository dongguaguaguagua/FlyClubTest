import os
# from .config import default_config
import openai

openai.organization = "org-WvMRPik8NGGoWxdJf9QPwpkh"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="code-davinci-003",
    prompt=["""
#include <stdio.h>

double getDoubleFromString(const char *str);
int i = 0;

/* 请在下面编写getDoubleFromString函数 */
int main(void)
{
    char line[300];
    while (gets(line) != NULL)
    {
        double n;
        i = 0;
        n = getDoubleFromString(line);
        // while (n > 0)
        {
            printf("%f\n", n);
            // n = getDoubleFromString(line);
        }
    }
    return 0;
}

// 编写getDoubleFromString函数，该函数可以从字符串中取出正浮点数或整数，无数可取，则返回值小于0。
"""],
    max_tokens=2048,
    n=1,
    stop=None,
    # temperature=0.5,
)

response = response['choices'][0]['text']
print(response)

# print("ג 1 2 你的博客是怎么搭的？")
