<template>
    <div class="section">
      <h2 class="section-title">
        <i class="fas fa-briefcase"></i> 工作经历
      </h2>
      <div v-for="(job, index) in workExperience" :key="index" class="experience-item">
        <div class="item-header">
          <div class="item-title">工作经历 #{{ index + 1 }}</div>
          <div class="actions">
            <button class="btn btn-outline" @click="openPolishModal('work', index)">
              <i class="fas fa-magic"></i> 润色
            </button>
            <button class="btn btn-danger" @click="removeWorkExperience(index)">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </div>
        <div class="form-group">
          <label>公司名称</label>
          <input type="text" v-model="job.company">
        </div>
        <div class="form-group">
          <label>职位</label>
          <input type="text" v-model="job.position">
        </div>
        <div class="form-group">
          <label>时间</label>
          <input type="text" v-model="job.duration" placeholder="例如：2019年6月 - 2022年8月">
        </div>
        <div class="form-group">
          <label>工作描述</label>
          <textarea v-model="job.description"></textarea>
        </div>
      </div>
      <button class="btn btn-primary" @click="addWorkExperience">
        <i class="fas fa-plus"></i> 添加工作经历
      </button>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue'
  
  defineProps({
    workExperience: {
      type: Array,
      required: true
    }
  })
  
  const emit = defineEmits([
    'add-work-experience',
    'remove-work-experience',
    'open-polish-modal'
  ])
  
  const addWorkExperience = () => emit('add-work-experience')
  const removeWorkExperience = (index) => emit('remove-work-experience', index)
  const openPolishModal = (type, index) => emit('open-polish-modal', type, index)
  </script>