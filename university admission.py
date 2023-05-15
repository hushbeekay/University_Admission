name= input('enter your name: ')
print ('''
            YOU ARE WELCOME
        ''')
jambscore = float(input('enter your jambscore: '))
post_utme_score = float(input('enter your post_utme_score: '))
aggr_score = ((jambscore/8) + (post_utme_score/2))
faculty = input('enter the faculty of your choice (use s for science and a for art): ').lower()

if faculty=='s' or faculty== 'science':
    if aggr_score<49:
        print ('You have Failed to meet the admission Requirements')
elif aggr_score>=50 and aggr_score<=60:
        print ('You can apply for the following courses: Agric','Botany','Zoology','Biology')
elif aggr_score>=61 and aggr_score<=70:
        print ('You can apply for the following courses: Computer Sci', 'Statistics', 'Physchology')
elif aggr_score>=71 and aggr_score<=80:
        print('You can apply for the following courses: Veterinary', 'Math', 'Biochemistry')
else:
        print('Congratulations you can apply for the following courses: Medicine', 'Nursing')

if faculty=='a' or faculty== 'art':
    if aggr_score<49:
        print ('You have Failed to meet the admission Requirements')
elif aggr_score>=50 and aggr_score<=60:
        print ('You can apply for the following courses: History, International Studies, Music, Economics')
elif aggr_score>=61 and aggr_score<=70:
        print ('You can apply for the following courses: Thearter Arts, Political Science, Modern European Languages')
elif aggr_score>=71 and aggr_score<=80:
        print('You can apply for the following courses: CLA, Linguistics, Religion and Human Relation')
else:
        print('Congratulations you can apply for the following courses: Law, Mass Communication, Criminology and Security Studies')
