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
