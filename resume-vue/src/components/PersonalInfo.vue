<template>
    <div class="section">
      <h2 class="section-title">
        <i class="fas fa-user"></i> 基本信息
      </h2>
      <div class="form-group">
        <label for="name">姓名</label>
        <input type="text" id="name" :value="personalInfo.name" @input="updateField('name', $event.target.value)">
      </div>
      <div class="form-group">
        <label for="title">职位</label>
        <input type="text" id="title" :value="personalInfo.title" @input="updateField('title', $event.target.value)">
      </div>
      <div class="form-group">
        <label for="phone">电话</label>
        <input type="text" id="phone" :value="personalInfo.phone" @input="updateField('phone', $event.target.value)">
      </div>
      <div class="form-group">
        <label for="email">邮箱</label>
        <input type="email" id="email" :value="personalInfo.email" @input="updateField('email', $event.target.value)">
      </div>
      <div class="form-group">
        <label for="summary">个人简介</label>
        <textarea id="summary" :value="personalInfo.summary" @input="updateField('summary', $event.target.value)"></textarea>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue'
  
  const emit = defineEmits(['update:personalInfo'])
  
  const props = defineProps({
    personalInfo: {
      type: Object,
      required: true
    }
  })
  
  const updateField = (field, value) => {
    emit('update:personalInfo', {
      ...props.personalInfo,
      [field]: value
    })
  }
  </script>