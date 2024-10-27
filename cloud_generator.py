from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import spacy


nlp = spacy.load('en_core_web_sm')

# если посмотреть не сохраняя
def plot_cloud(wordcloud): 
    # Set figure size 
    plt.figure(figsize=(40, 30)) 
    # Display image 
    plt.imshow(wordcloud)  
    # No axis details 
    plt.axis("off")
    
# кастомные цвета
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # вставляем слова, которые хотим выделить
    list_words=['school', 'town', 'teacher', 'walk', 'liquid']
    if word in list_words:
        return '#f79274'
    else:
        return "#20b1b0"
    
def clear_string(string):
    out = []
    string = string.lower().replace('wanna', 'want to')
    doc = nlp(string.strip().replace("n' ", "ng "))
    for token in doc:
        if not token.is_stop and token.is_alpha and len(token) > 2:
            if token.lemma_ not in out:
                out.append(token.lemma_)
    return ' '.join(out)
    
dir_name = input('Введите название директории с лирикой: ')
lyrics = []
for song in os.listdir(dir_name):
    with open(f'{dir_name}/{song}', encoding='utf-8') as f:
        file = ' '.join(f.readlines())
    lyrics.append(clear_string(file))
wordcloud = WordCloud(width=1600, height=800, background_color="#f7d4ca",
                     color_func=color_func).generate(' '.join(lyrics))
# сохранение файла
wordcloud.to_file(f'{dir_name}_wordcloud.png')