package com.cs222.nutrify.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.cs222.nutrify.databinding.FragmentUserpreferencesBinding

class UserPreferencesFragment : Fragment() {
    private lateinit var binding: FragmentUserpreferencesBinding

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        binding = FragmentUserpreferencesBinding.inflate(inflater, container, false)
        return binding.root
    }
}
