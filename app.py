import streamlit as st
import pandas as pd

from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Difference in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c
    return distance


try:
    with open('Log.txt','r') as f:
        data = f.read()
    data = data[-1]
except:
    data='0'
if int(data) > -1:
    st.title("Mystery Christmas Present!!!")

    st.markdown('''**Season's greetings!**''')
    st.markdown('To discover the meaning of Christmas (and who knows, perhaps the meaning of Christmas itself), you must solve a set of increasingly challenging puzzles, each one more infuriating than the last. Perhaps, there is no solution. Perhaps the true present was the puzzles you solved along the way....')
    st.markdown('''(It's ok, there is a real present. It may not be worth the next however many hours of pain but, I assure you, you would have been happy with it if I hadn't made you do this first. Remember that in six hours' time...)''' )
    but = st.button('''I'm ready for the first puzzle''')
    if but:
        with open('Log.txt','w') as f:
            f.write('1')
try:
    with open('Log.txt','r') as f:
        data = f.read()
        
    data = data[-1]
except:
    data='0'   

if int(data) > 0:
    st.title('Puzzle 1:')
    st.markdown('''Let's start off with something (reasonably) straightforward, just to check that the everything is working.''')
    st.markdown('The inside of a Christmas tree might be on a boat')
    answer = st.text_input('Type your answer here')
    if answer.lower() == 'mast':
        with open('Log.txt','w') as f:
            f.write('2')
        st.markdown('Correct!')
    else:
        if len(answer) > 0:
            
            st.markdown('''Hmmm, it's going to be a long Christmas...''')
            
try:
    with open('Log.txt','r') as f:
        data = f.read()
        
    data = data[-1]
except:
    data='0' 
if int(data) > 1:
    st.title('Puzzle 2:')
    st.markdown('''Don't worry, I haven't bought you a boat for Christmas. In fact, the present has nothing to do with a boat.''')
    st.markdown('''Next, we're going to actually work out an answer relevant to the present. How exciting.''')
    with open('WikiHoliday.txt','r') as f:
        data=f.read()
    data = data.split(' ')
    answer2 = st.text_input('Input your answer here. Some initial guesses may be helpful.').lower()
    if len(answer2) > 0:
        if answer2 == 'holiday' or answer2 == 'vacation':
            with open('Log.txt','w') as f:
                f.write('3')
            st.markdown('Correct!')
        else:
            first = 1e9
            count = 0
            for n,datum in enumerate(data):
                if datum.lower() == answer2:
                    count += 1
                    first = min(first,n)
                    word = data[n+1]
            if count == 0:
                st.write('This word does not appear')
            else:
                st.write('This word appears ' + str(count) + ' times, with the first appearance coming as word number ' + str(first+ 1) + '. The word immediately after its last appearance is **' + word + '**.')
try:
    with open('Log.txt','r') as f:
        data = f.read()
        
    data = data[-1]
except:
    data='0'                
if int(data) > 2:
    st.title('Puzzle 3:')
    st.markdown("So, you know it's a holiday. Unfortunately, because of what kind of holiday it actually is, and the way I've set this up, your expectations are now wildly overinflated. Don't let them stay that way. Remember that the person who's organised this holiday is the same person who decided that a set of puzzles would be a fun Christmas activity. That person has not booked you what might be described as a particularly nice holiday.")
    st.markdown("Of course, we now need to work out where the holiday is. Good luck, because all you have is this very faulty sat-nav. Oh, it's bad. Although bad actually works as an entry in it. Something to think about.")
    df = pd.read_csv('uk-towns.csv')[['latitude','longitude','postcode_area']]
    
    lat1 =51.63837
    lon1 =-2.67332
    mapping = {'a': '1 ',
 'b': '2 ',
 'c': '3 ',
 'd': '4 ',
 'e': '5 ',
 'f': '6 ',
 'g': '7 ',
 'h': '8 ',
 'i': '9 ',
 'j': '10',
 'k': '11',
 'l': '12',
 'm': '13',
 'n': '14',
 'o': '15',
 'p': '16',
 'q': '17',
 'r': '18',
 's': '19',
 't': '20',
 'u': '21',
 'v': '22',
 'w': '23',
 'x': '24',
 'y': '25',
 'z': '26'}
    
    df['postcode_area'] = [d[:4] for d in df['postcode_area'] ]
    st.write('_____________________________')
    text = st.text_input('Satnav entry').lower()
    if len(text) < 2:
        st.markdown('Too short!')
    else:
        lat = df[df['postcode_area'] == text[:2].upper() + mapping[text[2]]].to_numpy()
        if len(lat) == 0:
            st.markdown("Oh no! This didn't work!")
        else:
            lat2 = lat[0,0]
            lon2 = lat[0,1]
            d = calculate_distance(lat1, lon1, lat2, lon2)
            st.markdown('This journey would be ' + str(round(d)) + ' kilometres as the crow flies.')
    st.write('_____________________________')
    
    ans = st.text_input('Your final answer').lower()
    if ans.lower() == 'chepstow':
        with open('Log.txt','w') as f:
                f.write('4')
        st.markdown('Correct!')
    elif len(ans) > 0:
        st.markdown("Incorrect! Looks like you need to use the sat-nav again. It's stupid, I know (another entry that works though...)")
try:
    with open('Log.txt','r') as f:
        data = f.read()
        
    data = data[-1]
except:
    data='0'                
if int(data) > 3:
    st.title('Puzzle 4:')
    st.markdown("Well, you know what the present is. You know where it is. I imagine you've figured out when it is based on the location. (You might not have. But there's no puzzle to help you anyway).")
    
    st.markdown("Still, there's one more task, which is to find the Airbnb it's in. Ooh, difficult." )
    st.markdown('It might help you to know that Airbnb URLs are of the form https://www.airbnb.co.uk/rooms/ [EIGHT DIGIT NUMBER]. So, really (joy of joys) we just need a puzzle to get you to find a number. Good luck.....')
    cal1 = st.text_input('Your answer (or at least, your guess) here.').lower()
    if len(cal1) > 0:
        if len(cal1) != 8:
            st.markdown('Clearly wrong. I told you it was 8 digits!')
        else:
            try:
                _ = int(cal1)
            except:
                st.markdown("Ok, I know it's probably quite late, but it is a **number** we're looking for")
            true = '27322329'
            if cal1 == true:
                st.markdown("Correct! You've completed the puzzles!!! You win a holiday... that you'd already won...")
            else:
                mapping = {0: 'Holiday',
                          1: 'Egg',
                          2: 'Ribbon',
                          3: 'Sofa',
                          4: 'Despair',
                          5: 'Perhaps',
                          6: 'Pin',
                          7: 'Harpsichord',
                          8: 'Whimsy',
                          9: 'Wrath'}
                output = ''
                
                for n in range(8):
                    diff = (int(true[n])-int(cal1[n]))%10
                    output += mapping[diff]
                    output+=', '
                st.write(output)
            


  


        
        

            
        
    