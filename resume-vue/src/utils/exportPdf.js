import html2pdf from 'html2pdf.js'

export const exportToPDF = async (elementId, fileName) => {
    try {
        // 等待DOM完全加载
        const checkElement = () => {
            const element = document.getElementById(elementId)
            if (element) {
                return element
            }
            return null
        }

        let element = checkElement()
        if (!element) {
            // 如果未找到，等待500ms再试一次
            await new Promise(resolve => setTimeout(resolve, 500))
            element = checkElement()
            if (!element) {
                console.error(`未找到ID为${elementId}的导出元素`)
                return
            }
        }

        const opt = {
            margin: 10,
            filename: `${fileName}.pdf`,
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: {
                scale: 2,
                logging: false, // 禁用html2canvas日志
                useCORS: true // 启用跨域资源处理
            },
            jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
        }

        // 使用Promise处理导出
        html2pdf()
            .set(opt)
            .from(element)
            .save()
            .catch(err => {
                console.error('PDF导出失败:', err)
                alert('PDF导出失败，请禁用广告拦截插件后重试')
            })
    } catch (err) {
        console.error('导出过程中发生错误:', err)
        alert('导出过程中发生错误: ' + err.message)
    }
}