package com.cs222.nutrify.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class NutritionInputViewModel : ViewModel() {

    val input: MutableLiveData<MutableList<Int>> by lazy {
        MutableLiveData<MutableList<Int>>()
    }
}
