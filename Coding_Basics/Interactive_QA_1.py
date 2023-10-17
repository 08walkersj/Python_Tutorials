#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:25:01 2023

@author: simon
"""

import matplotlib.pyplot as plt
import numpy as np
import functools
import warnings
lw=5
# from matplotlib.widgets import Button
def check(button_axes):
    if not button_axes[-1, -1].checked:
        for ax in button_axes[0, :]:
            if ax.Question.result():
                ax.Question.text.append(ax.text(.5, .4, u"\u2714", zorder=-1, color='limegreen', size=120, 
                        va='center', ha='center'))
                if ax.Question.plotted:
                    for p in ax.Question.plotted: p.set_color('limegreen')
            else:
                ax.Question.text.append(ax.text(.5, .4, u"\u2716", zorder=-1, color='red', size=120,
                        va='center', ha='center'))
                if ax.Question.plotted:
                    for p in ax.Question.plotted: p.set_color('red')
                    ax.Question.plotted.extend(fig_ax.plot([ax.x, ax.Question.true_answer_ax.x],
                        [ax.y, ax.Question.true_answer_ax.y], color='limegreen', lw=lw))
                else:
                    ax.Question.plotted= fig_ax.plot([ax.x, ax.Question.true_answer_ax.x],
                        [ax.y, ax.Question.true_answer_ax.y], color='limegreen', lw=lw)
        button_axes[-1, -1].writing.remove()
        button_axes[-1, -1].writing= button_axes[-1, -1].text(0.5, 0.5, 'Next', 
                                                              color='white', 
                                                              va='center', 
                                                              ha='center',size=20)
        button_axes[-1, -1].set_facecolor('black')
        button_axes[-1, -1].checked=True
        plt.draw()
    else:
        for ax in button_axes[0, :]:
            if ax.Question.plotted:
                for p in ax.Question.plotted: p.remove()
            ax.Question.clicked=False
            for t in ax.Question.text: t.remove()
        plt.draw()
        
        return setup()
class Question(object):
    def __init__(self, answer, axis, axis2):
        self.true_answer= answer
        self.question_ax= axis
        self.true_answer_ax= axis2
        self.user_answer=False
        Question.plotted=False
    def result(self):
        return self.true_answer== self.user_answer
def onclick(button_axes, event):
    bools_left= np.array([axis.in_axes(event) for axis in button_axes[0]])
    bools_right= np.array([axis.in_axes(event) for axis in button_axes[1]])
    
    clicked_left= np.array([axis.clicked for axis in button_axes[0]])
    clicked_right= np.array([axis.clicked for axis in button_axes[1]])
    if bools_right[-1]:
        return check(button_axes)
    else:
        if any(bools_left) and any(clicked_right):
            if sum(bools_left)>1 or sum(clicked_right)>1:
                raise ValueError('multiple in axes left or clicked right')
            if button_axes[0, bools_left][0].Question.plotted:
                for p in button_axes[0, bools_left][0].Question.plotted: p.remove()
                button_axes[0, bools_left][0].Question.plotted=False
            button_axes[0, bools_left][0].Question.plotted=fig_ax.plot([button_axes[0, bools_left][0].x, button_axes[1, clicked_right][0].x],
                        [button_axes[0, bools_left][0].y, button_axes[1, clicked_right][0].y], 
                        color='darkblue', lw=lw)
            button_axes[0, bools_left][0].Question.user_answer= button_axes[1, clicked_right][0].answer
            button_axes[0, bools_left][0].clicked=False
            button_axes[1, clicked_right][0].clicked=False
        elif any(bools_left):
            if sum(bools_left)>1:
                raise ValueError('multiple in axes left')
            for axis in button_axes[0]: axis.clicked=False
            button_axes[0, bools_left][0].clicked=True
        elif any(bools_right) and any(clicked_left):
            if sum(bools_right)>1 or sum(clicked_left)>1:
                raise ValueError('multiple in axes right or clicked left')
            if button_axes[0, clicked_left][0].Question.plotted:
                for p in button_axes[0, clicked_left][0].Question.plotted: p.remove()
                button_axes[0, clicked_left][0].Question.plotted=False
            button_axes[0, clicked_left][0].Question.plotted=fig_ax.plot([button_axes[0, clicked_left][0].x, button_axes[1, bools_right][0].x],
                        [button_axes[0, clicked_left][0].y, button_axes[1, bools_right][0].y], 
                        color='darkblue', lw=lw)
                
            button_axes[0, clicked_left][0].Question.user_answer= button_axes[1, bools_right][0].answer
            button_axes[0, clicked_left][0].clicked=False
            button_axes[1, bools_right][0].clicked=False
        elif any(bools_right):
            if sum(bools_left)>1:
                raise ValueError('multiple in axes left')
            for axis in button_axes[1]: axis.clicked=False
            button_axes[1, bools_right][0].clicked=True
        else:
            raise warnings.warn('Did not click inside box!')
    plt.draw()
        
        
        
    
    
    
    
    
fig= plt.figure()
gs= fig.add_gridspec(6, 3, hspace=0, wspace=0)
fig_ax= fig.add_subplot(111)
fig_ax.axis(False)
fig_ax.set_ylim(0, 6)
fig_ax.set_xlim(-1, 1)
fig_ax.set_zorder(10)
fig_ax.set_facecolor(None)
button_axes= np.array([[fig.add_subplot(gs[i, 0]) for i in range(6)], 
                        [fig.add_subplot(gs[i, -1]) for i in range(6)]])
DPI=fig.get_dpi()
fig.set_size_inches(950.0/float(DPI),900.0/float(DPI))
onclick_wrapper=functools.partial(onclick, button_axes)
cid = fig.canvas.mpl_connect('button_press_event', onclick_wrapper)
for ax in button_axes.flatten():
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    ax.clicked=False
for j, (ax1, ax2) in enumerate(zip(*button_axes)):
    ax1.y= 6-(j+.5)
    ax2.y= 6-(j+.5)
    ax1.x= -.6
    ax2.x= .6
for ax, t in zip(button_axes[1, :].flatten(), ['string', 'integer', 'float', 'list', 'tuple']):
    ax.text(.5, .5, t, va='center', ha='center', size=23)
    ax.answer= t    
button_axes[-1, -1].writing=False

strings = ['hello', '15', '86 apples', 'gr8', 'spam', '0.5', '[1, 2]', '()']
def size_check(val):
    if len(val)>10:
        val= val.split(',')
        val_= []
        for v in range(len(val)//2):
            val_+=[val[v*2:(v+1)*2]]
        if len(val)%2:
            val=val_+val[:-len(val)%2]
        else:
            val= val_
        if len(val)>7:
            return True
    else:
        return False
def val2string(val):
    if isinstance(val, str):
        return f"'{val}'"
    elif isinstance(val, (int, float, np.int64)):
        return f"{val}"
    elif isinstance(val, list):
        while size_check(val):
            val= val[:-1]
        return f"{val}"
    elif isinstance(val, tuple):
        while size_check(val):
            val= val[:-1]
        return f"{val}"
    else:
        raise TypeError(f'Uknown Type {type(val)}')
def generate_iter(str_num, int_num, float_num, list_num, tuple_num, iter_type=list, sub_iter=False):
    if sub_iter:
        m=2
    else:
        m=6
    list_num= round((list_num-round(np.random.uniform(.4, 1, 1)[0],2))%1)
    tuple_num= round((tuple_num-round(np.random.uniform(.4, 1, 1)[0],2))%1)
    List=[]
    if list_num:
        List.append(generate_iter(np.random.randint(0, 2), np.random.randint(0, 2), 
                                np.random.randint(0, 2), np.random.randint(0, 1), 
                                np.random.randint(0, 1), sub_iter=True))
    if tuple_num:
        List.append(generate_iter(np.random.randint(0, 2), np.random.randint(0, 2), 
                              np.random.randint(0, 2), np.random.randint(0, 1),
                              np.random.randint(0, 1), iter_type=tuple, sub_iter=True))
    
    
    strings_cp= strings.copy()
    np.random.shuffle(strings_cp)
    
    List.extend(strings_cp[:str_num])
    List.extend(np.random.randint(0, 100, size=int_num))
    List.extend(np.round(np.random.uniform(0, 100, size=int_num), 3))
    np.random.shuffle(List)
    List= iter_type(List[:min([m, len(List)])])
    if sub_iter:
        return List
    else:
        return val2string(List)
def setup():
    if button_axes[-1, -1].writing:
       button_axes[-1, -1].writing.remove() 
    button_axes[-1, -1].writing=button_axes[-1, -1].text(0.5, 0.5, 'Check', color='white', va='center', ha='center', 
                             size=20)
    button_axes[-1, -1].set_facecolor('limegreen')
    lists=[generate_iter(2, 2, 2, 1, 1) for i in range(6)]
    tuples=[generate_iter(2, 2, 2, 1, 1, iter_type=tuple) for i in range(6)]
            
    integers= list(np.random.randint(0, 100, size=6))
    floats= list(np.round(np.random.uniform(0, 100, size=6), 3))
    
    strings_cp= strings.copy()
    strings_cp= [val2string(s) for s in strings_cp]
    np.random.shuffle(strings_cp)
    strings_cp= strings_cp[:6]
    all_vals= strings_cp+integers+floats+lists+tuples
    
    TS= ['string']*6+['integer']*6+ ['float']*6+ ['list']*6+ ['tuple']*6
    button_axes[-1, -1].checked=False

    ts= np.array(['string', 'integer', 'float', 'list', 'tuple'])

    
    for j, ax1 in zip(range(len(button_axes.T)), button_axes[0,:]):
        i= np.random.randint(0, len(all_vals), 1)[0]
        t= TS[i]
        val= all_vals[i]
        ax2= button_axes[1, np.append(ts==t, [False])][0]
        ax1.Question= Question(t, ax1, ax2)
        ax1.Question.value= val
        if t in ['list', 'tuple'] and len(val)>10:
            val= val.split(',')
            val_= ''
            for v in range(len(val)//2):
                val_+=','.join(val[v*2:(v+1)*2])+',\n'
            if len(val)%2:
                val=val_+ ','.join(val[-(len(val)%2):])
            else:
                val= val_[:-1]
            if val.endswith(','):
                val=val[:-1]
        ax1.Question.text= [ax1.text(0.5, 0.5, val, va='center', ha='center')]
        
        all_vals.remove(all_vals[i])
        TS.remove(t)
setup()