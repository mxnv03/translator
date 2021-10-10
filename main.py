from translate import Translator
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def translater():
    native = ''
    trans = ''
    lang = ''
    lang1 = ''
    lang_start = ''
    lang_edited = ''
    translated_message = ''
    code_dict = {'Russian': 'ru', 'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de',
                 'Русский': 'ru', 'Английский': 'en', 'Испанский': 'es', 'Французский': 'fr', 'Немецкий': 'de'}

    #translator = Translator()

    if request.method == 'POST':
        lang = request.form.get('lang')
        lang1 = request.form.get('lang1')
        trans = request.form.get('trans')  # запрос к данным формы

        if lang in code_dict.keys():
            lang_edited = code_dict[lang]
            lang_start = code_dict[lang1]

            translator = Translator(from_lang=lang_start, to_lang=lang_edited)
            translation = translator.translate(trans)
            #translated_message = translation.text
            return render_template('index.html', my_string=translation,
                                   lang='Your native language is _' + lang_start +
                                        '_ and your translation language is _' + lang_edited + '_')



    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)