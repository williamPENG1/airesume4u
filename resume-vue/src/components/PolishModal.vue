<template>
  <div class="modal-overlay" v-if="show">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">AI润色</h3>
        <button class="close-btn" @click="close">&times;</button>
      </div>

      <div class="form-group">
        <label>岗位介绍（可选）</label>
        <textarea v-model="jobDescription" placeholder="请输入目标岗位的详细信息，帮助AI更好地润色"></textarea>
      </div>

      <div class="form-group">
        <label>原始内容</label>
        <textarea :value="localOriginalContent" readonly style="background-color: #f8f9fa;"></textarea>
      </div>

      <button class="btn btn-primary" @click="polish" :disabled="isPolishing">
        <i class="fas fa-magic"></i> {{ isPolishing ? '润色中...' : '开始润色' }}
      </button>

      <div class="polish-result" v-if="result">
        <div class="result-title">润色结果</div>
        <div class="result-content">{{ result }}</div>
      </div>

      <div class="polish-result" v-if="reason">
        <div class="result-title">润色依据</div>
        <div class="result-content">{{ reason }}</div>
      </div>

      <div class="footer" v-if="result">
        <button class="btn btn-success" @click="applyResult">
          <i class="fas fa-check"></i> 应用润色结果
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, defineProps, defineEmits } from 'vue'

const props = defineProps({
  show: Boolean,
  originalContent: String
})

const emit = defineEmits(['close', 'apply'])

const jobDescription = ref('')
const result = ref('')
const reason = ref('')
const isPolishing = ref(false)
const localOriginalContent = ref('')

watch(() => props.originalContent, (newVal) => {
  localOriginalContent.value = newVal
}, { immediate: true })

const close = () => {
  jobDescription.value = ''
  result.value = ''
  reason.value = ''
  isPolishing.value = false
  emit('close')
}

const polish = async () => {
  isPolishing.value = true
  try {
    const response = await fetch('http://localhost:8000/prompt/polish', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        job_description: jobDescription.value || '通用技术岗位',
        project_content: props.originalContent
      })
    })

    const data = await response.json()
    result.value = data.polished_content
    reason.value = data.polish_reason
  } catch (error) {
    result.value = props.originalContent
    reason.value = '润色服务暂时不可用，请稍后重试'
    console.error('润色失败:', error)
  } finally {
    isPolishing.value = false
  }
}

const applyResult = () => {
  emit('apply', result.value)
  close()
}
</script>