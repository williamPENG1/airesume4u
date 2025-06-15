<template>
    <div class="section">
      <h2 class="section-title">
        <i class="fas fa-project-diagram"></i> 项目经历
      </h2>
      <div v-for="(project, index) in projectExperience" :key="index" class="project-item">
        <div class="item-header">
          <div class="item-title">项目经历 #{{ index + 1 }}</div>
          <div class="actions">
            <button class="btn btn-outline" @click="openPolishModal('project', index)">
              <i class="fas fa-magic"></i> 润色
            </button>
            <button class="btn btn-danger" @click="removeProjectExperience(index)">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </div>
        <div class="form-group">
          <label>项目名称</label>
          <input type="text" v-model="project.name">
        </div>
        <div class="form-group">
          <label>担任角色</label>
          <input type="text" v-model="project.role">
        </div>
        <div class="form-group">
          <label>时间</label>
          <input type="text" v-model="project.duration" placeholder="例如：2021年3月 - 2021年12月">
        </div>
        <div class="form-group">
          <label>项目描述</label>
          <textarea v-model="project.description"></textarea>
        </div>
      </div>
      <button class="btn btn-primary" @click="addProjectExperience">
        <i class="fas fa-plus"></i> 添加项目经历
      </button>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue'
  
  defineProps({
    projectExperience: {
      type: Array,
      required: true
    }
  })
  
  const emit = defineEmits([
    'add-project-experience',
    'remove-project-experience',
    'open-polish-modal'
  ])
  
  const addProjectExperience = () => emit('add-project-experience')
  const removeProjectExperience = (index) => emit('remove-project-experience', index)
  const openPolishModal = (type, index) => emit('open-polish-modal', type, index)
  </script>