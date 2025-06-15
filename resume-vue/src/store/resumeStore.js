import { reactive } from 'vue'

export const useResumeStore = () => {
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

    const addWorkExperience = () => {
        resumeData.workExperience.push({
            company: '',
            position: '',
            duration: '',
            description: ''
        })
    }

    const removeWorkExperience = (index) => {
        resumeData.workExperience.splice(index, 1)
    }

    const addProjectExperience = () => {
        resumeData.projectExperience.push({
            name: '',
            role: '',
            duration: '',
            description: ''
        })
    }

    const removeProjectExperience = (index) => {
        resumeData.projectExperience.splice(index, 1)
    }

    const addEducationExperience = () => {
        resumeData.educationExperience.push({
            school: '',
            degree: '',
            duration: '',
            description: ''
        })
    }

    const removeEducationExperience = (index) => {
        resumeData.educationExperience.splice(index, 1)
    }

    return {
        resumeData,
        addWorkExperience,
        removeWorkExperience,
        addProjectExperience,
        removeProjectExperience,
        addEducationExperience,
        removeEducationExperience
    }
}