<template>
  <div id="app">
    <header>
      <h1>简历生成器</h1>
      <div class="subtitle">使用Vue3创建专业简历，支持AI润色和PDF导出</div>
    </header>
    
    <div class="container">
      <!-- 编辑面板 -->
      <div class="editor-panel">
        <PersonalInfo 
          :personal-info="resumeData.personalInfo"
          @update:personal-info="(newData) => resumeData.personalInfo = newData"
        />
        <EducationExperience
          :education-experience="resumeData.educationExperience"
          :add-education-experience="addEducationExperience"
          :remove-education-experience="removeEducationExperience"
          @update-education="updateEducationExperience"
        />
        <WorkExperience 
          :work-experience="resumeData.workExperience"
          @add-work-experience="addWorkExperience"
          @remove-work-experience="removeWorkExperience"
          @open-polish-modal="openPolishModal"
        />
        <ProjectExperience 
          :project-experience="resumeData.projectExperience"
          @add-project-experience="addProjectExperience"
          @remove-project-experience="removeProjectExperience"
          @open-polish-modal="openPolishModal"
        />
      </div>
      
      <!-- 预览面板 -->
      <ResumePreview 
        :personal-info="resumeData.personalInfo"
        :work-experience="resumeData.workExperience"
        :project-experience="resumeData.projectExperience"
        :education-experience="resumeData.educationExperience"
      />
    </div>
    
    <!-- 控制面板 -->
    <div class="footer control-panel">
      <div class="control-group">
        <label>基础字号</label>
        <input type="range" min="12" max="20" step="1" v-model="fontSize" @input="updateStyles">
        <span>{{ fontSize }}px</span>
      </div>
      
      <div class="control-group">
        <label>行高</label>
        <input type="range" min="1.2" max="2.0" step="0.1" v-model="lineHeight" @input="updateStyles">
        <span>{{ lineHeight }}</span>
      </div>
      
      <div class="control-group">
        <label>段落间距</label>
        <input type="range" min="0.5" max="2.0" step="0.1" v-model="paragraphSpacing" @input="updateStyles">
        <span>{{ paragraphSpacing }}em</span>
      </div>
      
      <button class="btn export-btn" @click="() => exportToPDF('resume-content', 'my-resume')">
        <i class="fas fa-file-pdf"></i> 导出PDF
      </button>
    </div>
    
    <!-- AI润色模态框 -->
    <PolishModal 
      :show="showPolishModal" 
      :original-content="originalContent"
      @close="showPolishModal = false"
      @apply="applyPolishResult"
    />
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import PersonalInfo from './components/PersonalInfo.vue'
import WorkExperience from './components/WorkExperience.vue'
import ProjectExperience from './components/ProjectExperience.vue'
import EducationExperience from './components/EducationExperience.vue'
import ResumePreview from './components/ResumePreview.vue'
import PolishModal from './components/PolishModal.vue'
import { exportToPDF } from 'resume-vue/src/utils/exportPdf'

// 简历数据
const resumeData = reactive({
  personalInfo: {
    name: '张明',
    title: '高级前端工程师',
    phone: '13800138000',
    email: 'zhangming@example.com',
    summary: '拥有5年前端开发经验，精通Vue、React等前端框架，有丰富的跨平台开发经验。热爱技术，善于解决复杂问题，注重用户体验和代码质量。'
  },
  workExperience: [
    {
      company: '科技创新有限公司',
      position: '高级前端工程师',
      duration: '2020年3月 - 至今',
      description: '负责公司核心产品的前端架构设计和开发\n优化前端性能，提升页面加载速度30%\n带领5人前端团队，制定开发规范和代码审查\n使用Vue3重构旧版系统，提升开发效率和用户体验'
    },
    {
      company: '互联网科技有限公司',
      position: '前端开发工程师',
      duration: '2018年6月 - 2020年2月',
      description: '参与公司电商平台的前端开发\n实现响应式设计，确保在多种设备上的良好体验\n与后端团队协作，完成API对接和功能实现\n使用Webpack优化构建流程，减少构建时间40%'
    }
  ],
  projectExperience: [
    {
      name: '企业级后台管理系统',
      role: '前端负责人',
      duration: '2021年4月 - 2021年12月',
      description: '基于Vue3和Element Plus开发的后台管理系统\n实现权限管理、数据可视化、工作流引擎等核心模块\n采用微前端架构，实现模块化开发和部署\n优化前端性能，首屏加载时间减少50%'
    },
    {
      name: '移动端电商应用',
      role: '核心开发成员',
      duration: '2019年8月 - 2020年3月',
      description: '使用React Native开发的跨平台电商应用\n实现商品展示、购物车、支付等核心功能\n集成推送服务和第三方登录\n优化应用性能，减少内存占用30%，提升用户体验'
    }
  ],
  educationExperience: [
    {
      school: '清华大学',
      degree: '计算机科学与技术 硕士',
      duration: '2015年9月 - 2018年6月',
      description: '主修计算机科学与技术\nGPA: 3.8/4.0\n获得校级优秀毕业生称号'
    },
    {
      school: '北京大学',
      degree: '软件工程 学士',
      duration: '2011年9月 - 2015年6月',
      description: '主修软件工程\n获得国家奖学金\n担任学生会技术部部长'
    }
  ]
})

// 添加工作经历
const addWorkExperience = () => {
  resumeData.workExperience.push({
    company: '',
    position: '',
    duration: '',
    description: ''
  })
}

// 删除工作经历
const removeWorkExperience = (index) => {
  resumeData.workExperience.splice(index, 1)
}

// 添加项目经历
const addProjectExperience = () => {
  resumeData.projectExperience.push({
    name: '',
    role: '',
    duration: '',
    description: ''
  })
}

// 删除项目经历
const removeProjectExperience = (index) => {
  resumeData.projectExperience.splice(index, 1)
}

// 更新教育经历
const updateEducationExperience = ({ index, field, value }) => {
  resumeData.educationExperience[index][field] = value
  // 更新duration字段
  if (field === 'startYear' || field === 'endYear') {
    const edu = resumeData.educationExperience[index]
    edu.duration = `${edu.startYear || ''}年 - ${edu.endYear || ''}年`
  }
}

// 添加教育经历
const addEducationExperience = () => {
  const currentYear = new Date().getFullYear()
  resumeData.educationExperience.push({
    school: '',
    degree: '',
    startYear: currentYear - 4,
    endYear: currentYear,
    duration: `${currentYear - 4}年 - ${currentYear}年`,
    description: ''
  })
}

// 删除教育经历
const removeEducationExperience = (index) => {
  resumeData.educationExperience.splice(index, 1)
}

// AI润色相关状态
const showPolishModal = ref(false)
const originalContent = ref('')
const currentPolishType = ref('')
const currentPolishIndex = ref(-1)

// 打开润色模态框
const openPolishModal = (type, index) => {
  currentPolishType.value = type
  currentPolishIndex.value = index
  
  if (type === 'work') {
    originalContent.value = resumeData.workExperience[index].description
  } else if (type === 'project') {
    originalContent.value = resumeData.projectExperience[index].description
  }
  
  showPolishModal.value = true
}

// 应用润色结果
const applyPolishResult = (polishedText) => {
  if (currentPolishType.value === 'work') {
    resumeData.workExperience[currentPolishIndex.value].description = polishedText
  } else if (currentPolishType.value === 'project') {
    resumeData.projectExperience[currentPolishIndex.value].description = polishedText
  }
  showPolishModal.value = false
}

// 样式控制
const fontSize = ref(16)
const lineHeight = ref(1.6)
const paragraphSpacing = ref(1.0)

const updateStyles = () => {
  const previewEl = document.querySelector('.resume-preview')
  if (previewEl) {
    previewEl.style.setProperty('--base-font-size', `${fontSize.value}px`)
    previewEl.style.setProperty('--line-height', lineHeight.value)
    previewEl.style.setProperty('--paragraph-spacing', `${paragraphSpacing.value}em`)
  }
}

onMounted(() => {
  updateStyles()
})

// 使用从utils/exportPdf导入的exportToPDF函数
</script>

<style>
/* 全局样式 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Noto Sans SC', sans-serif;
}

/* 教育经历分段编辑样式 */
.education-section {
  margin-bottom: 25px;
  padding: 20px;
  background: #f9fafc;
  border-radius: 8px;
  border: 1px solid #eaeef5;
}

.education-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.education-fields {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 15px;
  margin-bottom: 15px;
}

.education-actions {
  display: flex;
  justify-content: flex-end;
}

.delete-btn {
  background: none;
  border: none;
  color: #dc3545;
  cursor: pointer;
  font-size: 16px;
  transition: opacity 0.2s;
}

.delete-btn:hover {
  opacity: 0.8;
}

body {
  background-color: #f5f7fa;
  color: #333;
  line-height: 1.6;
}

#app {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
  min-height: 100vh;
}

header {
  text-align: center;
  margin-bottom: 30px;
  padding: 20px 0;
  background: linear-gradient(135deg, #1e5799 0%,#207cca 51%,#2989d8 100%);
  color: white;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
}

.container {
  display: flex;
  gap: 30px;
  margin-bottom: 40px;
}

.editor-panel {
  flex: 1;
  background: white;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  max-width: 600px;
}

.preview-panel {
  flex: 1;
  background: white;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  min-height: 800px;
}

.section {
  margin-bottom: 25px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.section-title {
  font-size: 1.4rem;
  margin-bottom: 20px;
  color: #1e5799;
  display: flex;
  align-items: center;
}

.section-title i {
  margin-right: 10px;
}

.form-group {
  margin-bottom: 18px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #555;
}

input, textarea {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

input:focus, textarea:focus {
  border-color: #2989d8;
  outline: none;
  box-shadow: 0 0 0 2px rgba(41, 137, 216, 0.2);
}

textarea {
  min-height: 100px;
  resize: vertical;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.btn i {
  margin-right: 8px;
}

.btn-primary {
  background: #2989d8;
  color: white;
}

.btn-primary:hover {
  background: #1e71bb;
}

.btn-success {
  background: #28a745;
  color: white;
}

.btn-success:hover {
  background: #218838;
}

.btn-danger {
  background: #dc3545;
  color: white;
}

.btn-danger:hover {
  background: #bd2130;
}

.btn-outline {
  background: transparent;
  border: 1px solid #2989d8;
  color: #2989d8;
}

.btn-outline:hover {
  background: rgba(41, 137, 216, 0.1);
}

.experience-item, .project-item {
  background: #f9fafc;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  border: 1px solid #eaeef5;
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.item-title {
  font-weight: 600;
  font-size: 1.1rem;
}

.actions {
  display: flex;
  gap: 10px;
}

.resume-header {
  text-align: center;
  padding-bottom: 25px;
  margin-bottom: 25px;
  border-bottom: 2px solid #1e5799;
}

.resume-name {
  font-size: 2.2rem;
  font-weight: 700;
  color: #1e5799;
  margin-bottom: 8px;
}

.resume-title {
  font-size: 1.4rem;
  color: #555;
  margin-bottom: 15px;
}

.resume-contact {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 15px;
  color: #555;
}

.resume-section-title {
  font-size: 1.5rem;
  color: #1e5799;
  margin: 25px 0 15px;
  padding-bottom: 5px;
  border-bottom: 1px solid #eaeef5;
}

.resume-item {
  margin-bottom: 20px;
  transition: all 0.3s ease;
}

.resume-item:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.resume-item-header {
  display: flex;
  justify-content: space-between;
  font-weight: 600;
  margin-bottom: 5px;
}

.resume-item-title {
  font-size: 1.1rem;
}

.resume-item-date {
  color: #666;
  font-weight: 500;
}

.resume-item-subtitle {
  color: #2989d8;
  font-style: italic;
  margin-bottom: 8px;
}

.resume-item-content {
  color: #444;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  width: 90%;
  max-width: 700px;
  border-radius: 12px;
  padding: 30px;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-title {
  font-size: 1.5rem;
  color: #1e5799;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #777;
}

.polish-result {
  margin-top: 20px;
  padding: 15px;
  background: #f0f8ff;
  border-radius: 8px;
}

.result-title {
  font-weight: 600;
  margin-bottom: 10px;
  color: #1e5799;
}

.result-content {
  white-space: pre-wrap;
  line-height: 1.6;
}

.footer.control-panel {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  padding: 20px;
  gap: 25px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  margin-top: 30px;
}

.control-group {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 200px;
}

.control-group label {
  font-weight: 500;
  color: #555;
  min-width: 80px;
  text-align: right;
}

.control-group input[type="range"] {
  flex: 1;
  min-width: 100px;
}

.control-group span {
  min-width: 40px;
  text-align: center;
  font-weight: 500;
}

.export-btn {
  background: #28a745;
  padding: 12px 30px;
  font-size: 1.1rem;
  margin-left: 15px;
}

@media (max-width: 768px) {
  .footer.control-panel {
    flex-direction: column;
    align-items: stretch;
    gap: 15px;
  }
  
  .control-group {
    width: 100%;
  }
  
  .export-btn {
    margin-left: 0;
    margin-top: 10px;
  }
}

.export-btn i {
  margin-right: 10px;
}

@media (max-width: 900px) {
  .container {
    flex-direction: column;
  }
  
  .editor-panel, .preview-panel {
    max-width: 100%;
  }
}
</style>