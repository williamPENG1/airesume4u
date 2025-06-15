<template>
    <div class="preview-panel resume-preview" id="resume-content">

        <div class="resume-header">
          <div class="resume-name">{{ personalInfo.name }}</div>
          <div class="resume-title">{{ personalInfo.title }}</div>
          <div class="resume-contact">
            <span><i class="fas fa-phone"></i> {{ personalInfo.phone }}</span>
            <span><i class="fas fa-envelope"></i> {{ personalInfo.email }}</span>
          </div>
        </div>
        
        <div v-if="personalInfo.summary">
          <h3 class="resume-section-title">个人简介</h3>
          <div class="resume-item-content">{{ personalInfo.summary }}</div>
        </div>
        
        <div v-if="educationExperience.length">
          <h3 class="resume-section-title">教育经历</h3>
          <div class="education-header" style="display: grid; grid-template-columns: 2fr 2fr 1fr; gap: 16px; margin-bottom: 8px; font-weight: bold;">
          
        </div>
        <div v-for="(education, index) in educationExperience" :key="index" class="resume-item">
            <div class="education-container">
              <div class="education-item">{{ education.school }}</div>
              <div class="education-item resume-item-degree">{{ education.degree }}</div>
              <div class="education-item resume-item-date">{{ education.duration }}</div>
            </div>
        </div>
        
        <div v-if="workExperience.length">
          <h3 class="resume-section-title">工作经历</h3>
          <div v-for="(job, index) in workExperience" :key="index" class="resume-item">
            <div class="resume-item-header">
              <div class="resume-item-title">{{ job.company }}</div>
              <div class="resume-item-date">{{ job.duration }}</div>
            </div>
            <div class="resume-item-subtitle">{{ job.position }}</div>
            <div class="resume-item-content" style="white-space: pre-wrap;">{{ job.description }}</div>
          </div>
        </div>
        
        <div v-if="projectExperience.length">
          <h3 class="resume-section-title">项目经历</h3>
          <div v-for="(project, index) in projectExperience" :key="index" class="resume-item">
            <div class="resume-item-header">
              <div class="resume-item-title">{{ project.name }}</div>
              <div class="resume-item-date">{{ project.duration }}</div>
            </div>
            <div class="resume-item-subtitle">{{ project.role }}</div>
            <div class="resume-item-content" style="white-space: pre-wrap;">{{ project.description }}</div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'

  
  defineProps({
    personalInfo: {
      type: Object,
      required: true
    },
    workExperience: {
      type: Array,
      default: () => []
    },
    projectExperience: {
      type: Array,
      default: () => []
    },
    educationExperience: {
      type: Array,
      default: () => []
    }
  })
  </script>

<style scoped>
.preview-panel {
  padding: 30px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
}

.education-container {
  display: grid;
  grid-template-columns: 2fr 2fr 1fr;
  gap: 16px;
  align-items: center;
  margin-bottom: 10px;
}

.education-item {
  display: flex;
  flex-direction: column;
}

.resume-item-degree {
  font-style: italic;
}

@media (max-width: 600px) {
  .education-container,
  .education-header {
    grid-template-columns: 1fr;
    gap: 8px;
  }
  
  .education-header div {
    display: none;
  }
  
  .education-header div:first-child {
    display: block;
    font-weight: bold;
    grid-column: 1;
  }
}
</style>