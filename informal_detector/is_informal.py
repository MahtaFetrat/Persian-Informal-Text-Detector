import re


# **NOTE:** The roots and some of the words used above are form this [link](https://fa.wikipedia.org/wiki/%D9%88%DB%8C%DA%A9%DB%8C%E2%80%8C%D9%BE%D8%AF%DB%8C%D8%A7:%D8%A7%D8%B4%D8%AA%D8%A8%D8%A7%D9%87%E2%80%8C%DB%8C%D8%A7%D8%A8/%D9%81%D9%87%D8%B1%D8%B3%D8%AA/%D8%BA%DB%8C%D8%B1%D8%B1%D8%B3%D9%85%DB%8C).
words = ['توش', 'آتیش', 'توی', 'همونطور', 'اگه', 'تیکه', 'یهو', 'واسه', 'واسم', 'واست', 'واسش', 'واسمون', 'واستون', 'واسشون', 'رمضون', 'دیگه', 'اینا', 'اونا', 'بهش', 'هیچی', 'برام', 'برات', 'برامون', 'براشون', 'براتون', 'براش', 'والا', 'دوس', 'ایش', 'هرچی', 'چی', 'آره', 'چطوری', 'چه\u200cطوری', 'چقد', 'یه', 'بارون', 'ازم', 'ازت', 'ازش', 'ازمون', 'ازتون', 'ازشون', 'اصن', 'اینو', 'اونو', 'اینارو', 'اونارو', 'زبون', 'بابا', 'بابام', 'بابات', 'باباش', 'بابامون', 'باباتون', 'باباشون', 'ماما', 'مامان', 'مامانم', 'مامانت', 'مامانمون', 'مامانتون', 'مامانشون', 'آسون', 'دیگه\u200cای', 'بهت', 'بهش', 'بهمون', 'بهتون', 'بهشون', 'خونه', 'جون', 'ایشالا', 'ماشالا', 'ایشون', 'اونه', 'اینجوری', 'بازم', 'باهام', 'باهات', 'باهاش', 'باهامون', 'باهاتون', 'باهاشون', 'تموم', 'چجوری', 'چیه', 'کدوم', 'آروم', 'ایرونی', 'بادمجون', 'بچگونه', 'بیابون', 'تهرون', 'دندون', 'خودتون', 'خودشون', 'خودمون', 'خودمونی', 'خیابون', 'داره', 'داروخونه', 'داغون', 'دخترونه', 'دندون', 'رودخونه', 'زمونه', 'زنونه', 'قلیون', 'مردونه', 'مهمون', 'میونه', 'میون', 'نشونه', 'نشون', 'نیستن', 'هستن', 'همزبون', 'همشون', 'پسرونه', 'کوچیک', 'تموم', 'تمومه', 'انقد']
roots1 = 'پاشون|[یا]فشون|پرورون|پرون|پوسون|پوشون|پیچون|تابون|تازون|ترسون|ترکون|تکون|جنبون|جوشون|چپون|چربون|چرخون|چرون|چسبون|چشون|چکون|چلون|خارون|خراشون|خشکون|خندون|خوابون|خورون|خون|خیسون|درخشون|رسون|رقصون|رنجون|رون|سابون|ستون|سوزون|شورون|غلتون|فهمون|کوبون|گذرون|گردون|گریون|گسترون|گنجون|لرزون|لغزون|لمبون|مالون|نشون|وزون|تونست|دون|ش'
roots2 = 'پاشون|[یا]فشون|پرورون|پرون|پوسون|پوشون|پیچون|تابون|تازون|ترسون|ترکون|تکون|جنبون|جوشون|چپون|چربون|چرخون|چرون|چسبون|چشون|چکون|چلون|خارون|خراشون|خشکون|خندون|خوابون|خورون|خون|خیسون|درخشون|رسون|رقصون|رنجون|رون|سابون|ستون|سوزون|شورون|غلتون|فهمون|کوبون|گذرون|گردون|گریون|گسترون|گنجون|لرزون|لغزون|لمبون|مالون|وزون'
roots3 = 'خوا'
roots4 = 'مون|شین|گ'
roots5 = 'د|تون'
roots6 = 'یا'
roots7 = 'ر'


start_regex = '(?:\s|\.|\?|!|-|\+|=|\*|/|\\|\]|\[|\}|\{|"|\'|;|؛|,|#|$\|%|\(|\)|،|«|»|؟|^)'
end_regex = '(?:\s|\.|\?|!|-|\+|=|\*|/|\\|\]|\[|\}|\{|"|\'|;|؛|,|#|$\|%|\(|\)|،|«|»|؟|$)'

regexes = [
start_regex + r'(?:' + '|'.join(re.escape(word) for word in words) + r')' + end_regex,
start_regex + r'(?:(?:ب|ن)|(?:(?:می|نمی)[\s\u200c]*))(?:' + roots1 + r')(?:م|ی|ه|یم|ید|ین|ن)' + end_regex,
start_regex + r'(?:' + roots2 + r')د(?:م|ی||یم|ید|ین|ن)(?:\b|،|«|»|؟|$)',
start_regex + r'(?:(?:ب|ن)|(?:(?:می|نمی)[\s\u200c]*))(?:' + roots3 + r')(?:م|ی|یم|ید|ین)' + end_regex,
start_regex + r'(?:ب|(?:(?:می|نمی)[\s\u200c]*))(?:' + roots4 + r')(?:م|ی|ه|یم|ید|ین|ن)' + end_regex,
start_regex + r'(?:ن|(?:(?:می|نمی)[\s\u200c]*))(?:' + roots5 + r')(?:م|ی|ه|یم|ید|ین|ن)' + end_regex,
start_regex + r'(?:ن|نمی[\s\u200c]*)(?:' + roots6 + r')(?:م|ه|یم|ید|ین|ن)' + end_regex,
start_regex + r'می[\s\u200c]*(?:' + roots7 + r')(?:م|ی|ه|یم|ید|ین|ن)' + end_regex,
]


def is_informal(text, threshold=1):
    matches = 0
    for regex in regexes:
        matches += len(re.findall(regex, text))

    return True if matches >= threshold else False
