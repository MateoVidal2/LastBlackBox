# -*- coding: utf-8 -*-
"""
LBB: Task Class

@author: kampff
"""

# Import libraries
import os

# Import modules

# Task Class
class Task:
    def __init__(self, text=None):
        self.name = None            # name
        self.description = None     # description
        if text:
            self.parse(text)
        return
    
    def parse(self, text):
        self.name = "TASK\n"
        return
    
    def render(self):
        return self.name

#FIN