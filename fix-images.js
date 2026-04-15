/**
 * 图片加载修复脚本
 * 确保所有图片都能正常显示
 */
(function() {
    'use strict';

    // 页面加载完成后执行
    function fixImages() {
        // 查找所有使用懒加载的图片
        const lazyImages = document.querySelectorAll('img[data-raw-src]');
        
        lazyImages.forEach(function(img) {
            const realSrc = img.getAttribute('data-raw-src');
            if (realSrc && realSrc !== img.src) {
                // 直接设置真实图片URL
                img.src = realSrc;
                
                // 添加错误处理
                img.onerror = function() {
                    console.warn('图片加载失败:', realSrc);
                    // 如果远程图片加载失败，保持占位图
                    this.src = 'https://img.amz123.com/upload/index_icon/20210824/empty.png';
                };
            }
        });

        console.log('已修复', lazyImages.length, '张懒加载图片');
    }

    // 多种时机尝试修复
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', fixImages);
    } else {
        fixImages();
    }

    // 延迟再次检查
    setTimeout(fixImages, 1000);
    setTimeout(fixImages, 3000);

    // 监听DOM变化，处理动态添加的图片
    if (typeof MutationObserver !== 'undefined') {
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.addedNodes) {
                    mutation.addedNodes.forEach(function(node) {
                        if (node.nodeName === 'IMG' && node.getAttribute('data-raw-src')) {
                            const realSrc = node.getAttribute('data-raw-src');
                            if (realSrc && realSrc !== node.src) {
                                node.src = realSrc;
                            }
                        }
                        // 检查子元素
                        if (node.querySelectorAll) {
                            const imgs = node.querySelectorAll('img[data-raw-src]');
                            imgs.forEach(function(img) {
                                const realSrc = img.getAttribute('data-raw-src');
                                if (realSrc && realSrc !== img.src) {
                                    img.src = realSrc;
                                }
                            });
                        }
                    });
                }
            });
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }

})();
