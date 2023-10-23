from collections import Counter
# song="""Besuge Besuge Besuge Besuge
# Besuge Besuge Besuge Besuge
# Jeevanavella Sundara Besuge
# Besuge Besuge Besuge Besuge
# Besuge Besuge Besuge Besuge
# Jeevanavella Sundara Besuge
# Raagada Jothege Thalada Besuge
# Raaga Thalake Bhavada Besuge
# Raagada Jothege Thalada Besuge
# Raaga Thalake Bhavada Besuge
# Bhavada Jothege Geetheya Besuge
# Geetheya Jothe Sangeethada Besuge
# Besuge Besuge Besuge Besuge
# Jeevanavella Sundara Besuge
# Hareyada Hennige Lajjeya Besuge
# Miruguva Kannige Aaseya Besuge
# Hareyada Hennige Lajjeya Besuge
# Miruguva Kannige Aaseya Besuge
# Youanadalli Mohada Besuge
# Maimanadalli Bayakeya Besuge
# Besuge lala lala Besuge lala lala
# Besuge lala lala Besuge lala lala
# Jeevanavella Sundara Besuge
# Eradu Manasige Olavina Besuge
# Eradu Baalina Bandhana Besuge
# Eradu Manasige Olavina Besuge
# Eradu Baalina Bandhana Besuge
# Madhura Milanake Preetiya Besuge
# Januma Janumaku Aatmada Besuge
# Besuge Besuge Besuge Besuge
# Besuge Besuge Besuge Besuge
# Jeevanavella Sundara Besuge
# Besuge Besuge Besuge Besuge
# Besuge Besuge Besuge Besuge
# Januma Janumaku Aatmada Besuge"""
# song_list=song.split()
# tot_words=len(song_list)
# word_c=str(input("Enter  the word to be counted"))
# word_count=song_list.count(word_c)
# print("Total number of words in the song is",tot_words)
# print("total number of times the given word is repeated is",word_count)
# song_set=set(song_list)
# mod_list=list(song_set)
# i=0
# while(i<len(mod_list)):
#     print(mod_list[i])
#     print(song_list.count(mod_list[i]))
#     i=i+1


# using dictionaries to store data
song="""Besuge Besuge Besuge Besuge
Besuge Besuge Besuge Besuge
Jeevanavella Sundara Besuge
Besuge Besuge Besuge Besuge
Besuge Besuge Besuge Besuge
Jeevanavella Sundara Besuge
Raagada Jothege Thalada Besuge
Raaga Thalake Bhavada Besuge
Raagada Jothege Thalada Besuge
Raaga Thalake Bhavada Besuge
Bhavada Jothege Geetheya Besuge
Geetheya Jothe Sangeethada Besuge
Besuge Besuge Besuge Besuge
Jeevanavella Sundara Besuge
Hareyada Hennige Lajjeya Besuge
Miruguva Kannige Aaseya Besuge
Hareyada Hennige Lajjeya Besuge
Miruguva Kannige Aaseya Besuge
Youanadalli Mohada Besuge
Maimanadalli Bayakeya Besuge
Besuge lala lala Besuge lala lala
Besuge lala lala Besuge lala lala
Jeevanavella Sundara Besuge
Eradu Manasige Olavina Besuge
Eradu Baalina Bandhana Besuge
Eradu Manasige Olavina Besuge
Eradu Baalina Bandhana Besuge
Madhura Milanake Preetiya Besuge
Januma Janumaku Aatmada Besuge
Besuge Besuge Besuge Besuge
Besuge Besuge Besuge Besuge
Jeevanavella Sundara Besuge
Besuge Besuge Besuge Besuge
Besuge Besuge Besuge Besuge
Januma Janumaku Aatmada Besuge"""
song_list=song.split()
# tot_words=len(song_list)
# word_c=str(input("Enter  the word to be counted"))
# word_count=song_list.count(word_c)
# print("Total number of words in the song is",tot_words)
# print("total number of times the given word is repeated is",word_count)
# song_set=set(song_list)
# mod_list=list(song_set)
# song_dict={'word':'count'}
# i=0
# while(i<len(mod_list)):
#   cou = song_list.count(mod_list[i])
#   song_dict.update({mod_list[i]:cou})
#   i=i+1
# print(song_dict)
print(Counter(song_list))