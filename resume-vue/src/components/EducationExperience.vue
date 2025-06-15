<template>
  <div class="section">
    <h2 class="section-title">
        <i class="fas fa-briefcase"></i> 教育经历
    </h2>
    <div 
      v-for="(edu, index) in educationExperience" 
      :key="`edu-${index}-${edu.school}`" 
      class="education-section"
    >
    <div class="item-header">
      <div class="item-title">教育经历 #{{ index + 1 }}</div>
      <button class="btn btn-danger" @click="removeEducation(index)">
              <i class="fas fa-trash"></i>
      </button>
    </div>
      <div class="education-fields">
        <input 
          :value="edu.school" 
          @input="updateEducation(index, 'school', $event.target.value)"
          placeholder="学校名称" 
          class="resume-input"
        >
        
        <input 
          :value="edu.degree" 
          @input="updateEducation(index, 'degree', $event.target.value)"
          placeholder="学位/专业" 
          class="resume-input"
        >
        
        <div class="date-picker">
          <div class="date-range">
            <select
              :value="edu.startYear"
              @change="updateEducation(index, 'startYear', $event.target.value)"
              class="year-select"
            >
              <option value="">选择年份</option>
              <option v-for="year in years" :key="`start-year-${year}`" :value="year">
                {{ year }}年
              </option>
            </select>
            <select
              :value="edu.startMonth"
              @change="updateEducation(index, 'startMonth', $event.target.value)"
              class="month-select"
            >
              <option value="">选择月份</option>
              <option v-for="month in months" :key="`start-month-${month.value}`" :value="month.value">
                {{ month.label }}
              </option>
            </select>
          </div>
          <span>至</span>
          <div class="date-range">
            <select
              :value="edu.endYear"
              @change="updateEducation(index, 'endYear', $event.target.value)"
              class="year-select"
            >
              <option value="">选择年份</option>
              <option v-for="year in years" :key="`end-year-${year}`" :value="year">
                {{ year }}年
              </option>
            </select>
            <select
              :value="edu.endMonth"
              @change="updateEducation(index, 'endMonth', $event.target.value)"
              class="month-select"
            >
              <option value="">选择月份</option>
              <option v-for="month in months" :key="`end-month-${month.value}`" :value="month.value">
                {{ month.label }}
              </option>
            </select>
          </div>
        </div>
      </div>
      
      <textarea 
        :value="edu.description" 
        @input="updateEducation(index, 'description', $event.target.value)"
        placeholder="教育经历描述" 
        class="resume-textarea"
      ></textarea>
      
    </div>
    <button class="add-btn" @click="addEducation">
      <i class="fas fa-plus"></i> 添加教育经历
    </button>
  </div>
</template>

<style scoped>
.resume-input,
.year-select,
.month-select,
.resume-textarea {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s;
  background-color: white;
}

.resume-input:focus,
.resume-textarea:focus,
.year-select:focus,
.month-select:focus {
  border-color: #2989d8;
  outline: none;
  box-shadow: 0 0 0 2px rgba(41, 137, 216, 0.2);
}

.resume-textarea {
  min-height: 100px;
  resize: vertical;
}

.date-picker {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  width: 100%;
  margin: 12px 0;
}

.date-range {
  display: flex;
  gap: 6px;
  flex: 1;
  min-width: 0;
  max-width: calc(50% - 4px);
}

.year-select,
.month-select {
  flex: 1;
  min-width: 0;
  width: 100%;
  max-width: 100px;
}

.date-picker span {
  margin: 0 8px;
  color: #666;
  white-space: nowrap;
}

.year-select, 
.month-select {
  min-width: 115px;
  cursor: pointer;
}

.year-select option,
.month-select option {
  padding: 8px;
}

.add-btn {
  padding: 10px 20px;
  background: #2989d8;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  margin-top: 15px;
  transition: all 0.3s;
}

.add-btn:hover {
  background: #1e71bb;
}

.add-btn i {
  margin-right: 8px;
}

@media (max-width: 768px) {
  .date-picker {
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
  }
  
  .date-picker span {
    margin: 8px 0;
    text-align: center;
  }
  
  .date-range {
    width: 100%;
    max-width: 100%;
  }
  
  .year-select,
  .month-select {
    max-width: 100%;
  }
}
</style>

<script setup>
import { defineProps, computed, defineEmits } from 'vue'

const props = defineProps({
  educationExperience: {
    type: Array,
    default: () => []
  },
  addEducationExperience: {
    type: Function,
    required: true
  },
  removeEducationExperience: {
    type: Function,
    required: true
  }
})

const emit = defineEmits(['update-education'])

const currentYear = new Date().getFullYear()
const currentMonth = new Date().getMonth() + 1
const years = computed(() => {
  const startYear = 2000
  const years = []
  for (let year = currentYear; year >= startYear; year--) {
    years.push(year)
  }
  return years
})

const months = computed(() => {
  return Array.from({length: 12}, (_, i) => ({
    value: i + 1,
    label: `${i + 1}月`
  }))
})

const updateEducation = (index, field, value) => {
  emit('update-education', { index, field, value })
}

const addEducation = () => {
  props.addEducationExperience()
  // 通过emit更新初始时间
  emit('update-education', {
    index: props.educationExperience.length - 1,
    field: 'startYear',
    value: currentYear - 4
  })
  emit('update-education', {
    index: props.educationExperience.length - 1,
    field: 'startMonth',
    value: currentMonth
  })
  emit('update-education', {
    index: props.educationExperience.length - 1,
    field: 'endYear',
    value: currentYear
  })
  emit('update-education', {
    index: props.educationExperience.length - 1,
    field: 'endMonth',
    value: currentMonth
  })
}

const removeEducation = (index) => {
  props.removeEducationExperience(index)
}
</script>
