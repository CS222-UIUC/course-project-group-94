package com.cs222.nutrify.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.cs222.nutrify.databinding.FragmentNutritioninputBinding

class NutritionInputFragment : Fragment() {

    private lateinit var binding: FragmentNutritioninputBinding

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentNutritioninputBinding.inflate(inflater, container, false)
        return binding.root
    }
}
