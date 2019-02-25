# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:34:54 2019

@author: murie
"""

import sys
if "Tkinter" not in sys.modules:
    from tkinter import *

# read in bls_data_frame module
import bls_data_frame as b
# read in the match_indeed_to_skill module
import match_indeed_to_skill as mi
# read in the heinz_scraper module
import heinz_scraper as hs
import pandas as pd

# Get DF of BLS with Data
df_bls = b.get_df_bls()

# Get full list of BLS-tracked jobs
job_list = b.get_job_list(df_bls)

skill_dictionary = {'Financial Analyst':['Know how to analyze things I guess', 'Statistical analysis specifically'], 'Project Manager':'Dont hate people'}
course_dictionary = {'Financial Analyst':['Programming R for Analytics', 'Statistical Analysis for Analytics 101'], 'Project Manager':'Project Management 101'}

def skill_builder_interface(skill_dictionary, course_dictionary):

    # Create command for submit button
    def click():

        # Get Drop-down selection
        entered_text = variable.get()

        # Get full list of possible skills
        skill_list = mi.get_skill_list()

        # Set Job to drop-down text
        job = entered_text

        # Get Job_stats
        job_stats = b.get_job_stats(df_bls, job)

        #Get Indeed scrape
        job_df = mi.scrape_pages(job,'Pittsburgh','PA',skill_list)

        # Match skills - jobs
        job_skill_count = mi.return_job_count(skill_list,job_df)

        # Match skills to Heinz course listings
        skill_map = hs.get_skill_map(job_skill_count['Skill'].values)
        # turn courses into a printable format
        course_set = set()
        for i in skill_map.values():
            for j in i:
                course_set.add(j)
        course_pd = pd.DataFrame(list(course_set))

        output_job.delete(0.0, END)
        output_job.insert(END, job_stats)

        output_skills.delete(0.0, END)
        output_skills.insert(END, job_skill_count)

        output_courses.delete(0.0, END)
        output_courses.insert(END, course_pd.values)

    window = Tk()
    window.title("SkillBuilder")
    window.configure(bg="white")

    # add Heinz image
    photo1 = PhotoImage(file="Skill_Builder.gif")
    Label(window, image=photo1, bg="white").grid(row=0, column=0, sticky=W, columnspan=2)

    # Create job selection pull-down menu
    lbl_input = Label(window, text="Dream job?", bg="white", fg="red4", font="times 14 bold")
    lbl_input.grid(row=1, column=0, sticky=W)

    variable = StringVar(window)
    jobs = job_list
    variable.set("No Job Selected")

    textentry_menu = OptionMenu(window, variable, *jobs)
    textentry_menu.config(bg="red4", activebackground="red4", fg="white", activeforeground="white", font="times 10")
    textentry_menu.grid(row=2, column=0, columnspan=1, sticky = N+S+W+E, padx = 5, pady = 5)
    textentry = str(textentry_menu)

    # Create a "Submit" button
    submit_button = Button(window, text="Submit", width=8, command=click, activebackground="gray70", font="times 10")
    submit_button.grid(row=2, column=1, sticky=W)

    # Create text output sections
    lbl_output_skills = Label(window, text="\nSkills Needed:", bg="white", fg="red4", font="times 14 bold")
    lbl_output_skills.grid(row=4, column=0, sticky=W)
    output_skills = Text(window, width=35, height=6, wrap=WORD, bg="MistyRose2", bd=2)
    output_skills.grid(row=5, column=0, columnspan=1, sticky = N+S+W+E)

    lbl_output_courses = Label(window, text="\nCourses:", bg="white", fg="red4", font="times 14 bold")
    lbl_output_courses.grid(row=4, column=1, sticky=W)
    output_courses = Text(window, width=35, height=6, wrap=WORD, bg="MistyRose2", bd=2)
    output_courses.grid(row=5, column=1, columnspan=1, sticky = N+S+W+E)

    lbl_output_job = Label(window, text="\nJob Information:", bg="white", fg="red4", font="times 14 bold")
    lbl_output_job.grid(row=6, column=0, sticky=W)
    output_job = Text(window, width=35, height=6, wrap=WORD, bg="MistyRose2", bd=2)
    output_job.grid(row=7, column=0, columnspan=1, sticky = N+S+W+E)


    # Create an exit button
    def close_window():
        window.destroy()
        exit()

    Button(window, text="Exit", width=12, command=close_window, activebackground="gray70", font="times 10").grid(row=9, column=1, sticky=SE)

    window.mainloop()

skill_builder_interface(skill_dictionary, course_dictionary)
