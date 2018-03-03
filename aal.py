#!/usr/bin/env python3

import pyautogui

pyautogui.PAUSE     = 5
pyautogui.FAILSAFE  = True
iteration           = 1

# Start Alert
pyautogui.alert('Ready?')

# Main loop
while True:
    start_exam = pyautogui.locateCenterOnScreen('start_exam.png')
    if start_exam != None:
        pyautogui.click(start_exam)

        # Exam loop. Do until score test button appears
        while True:
            score_test_pos = pyautogui.locateCenterOnScreen('score_test.png')
            if score_test_pos != None:
                pyautogui.click(score_test_pos)
                score_anyway_pos = pyautogui.locateCenterOnScreen('score_anyway.png')
                pyautogui.click(score_anyway_pos)
                done_pos = pyautogui.locateCenterOnScreen('done.png')
                pyautogui.click(done_pos)
                break

            # Grab answer, take screenshot, +1 iteration, next question
            check_answer_pos = pyautogui.locateCenterOnScreen('check_answer.png')
            pyautogui.click(check_answer_pos)

            pyautogui.screenshot(str(iteration) +'.png')
            iteration += 1

            prt_sc_pos = pyautogui.locateCenterOnScreen('next_question.png')
            pyautogui.click(prt_sc_pos)

    next_question = pyautogui.locateCenterOnScreen('next_question.png')
    if next_question != None:
        pyautogui.click(next_question)

    # Sometimes the image is a bit off. Check for it:
    next_misc = pyautogui.locateCenterOnScreen('next_misc.png')
    if next_misc != None:
        pyautogui.click(next_misc)

    play_video = pyautogui.locateCenterOnScreen('play_video.png')
    if play_video != None:
        pyautogui.click(play_video)
        # Pause 1 min before continue
        pyautogui.moveTo(50,50,duration = 70)
        next_video = pyautogui.locateCenterOnScreen('next_video.png')
        pyautogui.click(next_video)

'''
pyautogui.dragTo(25, 25, duration = num_seconds)
pyautogui.dragRel(50, 50, duration = num_seconds)
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter
pyautogui.locateCenterOnScreen('looksLikeThis.png')  # returns center x and y
(898, 423)
pyautogui.screenshot('foo.png')  # returns a Pillow/PIL Image object, and saves it to a file
<PIL.Image.Image image mode=RGB size=1920x1080 at 0x31AA198>
'''
