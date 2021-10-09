def filter_symble(content):
    '''
    0. 文本全部转化为小写
    1. 对于文字内容的清洗部分
    --a.需要对emoji进行清洗处理
    --b.需要对空格，标点符号，中文&英文的标点符号进行清洗
    input:[string]txt column name
          [dataFrame] df
    output:[list]all words in one list(unduplicated)
    '''
    content = str.lower(content)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
                           "]+", flags=re.UNICODE)
    # no emoji for iphone and wechat
    remove_emoji_content = emoji_pattern.sub(r'', content)
    remove_emoji_content = re.sub(emoji.get_emoji_regexp(), r"", remove_emoji_content)
    # delect red specific emoji
    remove_red_spesific_emoji_r = re.sub(r'\[.+r\]',"",remove_emoji_content)
    remove_red_spesific_emoji_h = re.sub(r'\[.+h\]',"",remove_red_spesific_emoji_r)
    # remove Chinese punctuation
    remove_punctuation_chinese = re.sub(r"[%s]+" %z_punctuation, "", remove_red_spesific_emoji_h)
    # remove English punctuation
    remove_punctuation_english = re.sub(r"[%s]+" %punctuation, "", remove_punctuation_chinese)
    return remove_punctuation_english
