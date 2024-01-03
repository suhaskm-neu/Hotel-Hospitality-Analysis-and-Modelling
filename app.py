import streamlit as st
import pickle
import numpy as np

import traceback

# loading the trained model

pickle_in = open('hotel.pkl', 'rb')
