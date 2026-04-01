#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF转Markdown工具
将学术论文PDF转换为Markdown格式
"""

import pdfplumber
import re
import os

def extract_pdf_to_markdown(pdf_path, output_path):
    """
    提取PDF内容并转换为Markdown格式
    
    Args:
        pdf_path: PDF文件路径
        output_path: 输出Markdown文件路径
    """
    
    markdown_content = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"正在处理PDF文件，共 {total_pages} 页...")
        
        for page_num, page in enumerate(pdf.pages, 1):
            print(f"处理第 {page_num}/{total_pages} 页...")
            
            # 提取文本
            text = page.extract_text()
            
            if text:
                # 处理文本格式
                lines = text.split('\n')
                
                for line in lines:
                    line = line.strip()
                    
                    if not line:
                        continue
                    
                    # 识别标题（通常字体较大或加粗）
                    # 一级标题：论文标题
                    if page_num == 1 and len(line) > 20 and not line.startswith(' '):
                        if '类脑AGI架构' in line or 'TianYuan' in line:
                            markdown_content.append(f"# {line}\n")
                            continue
                    
                    # 识别章节标题
                    if re.match(r'^[一二三四五六七八九十]+[、\.]', line):
                        markdown_content.append(f"\n## {line}\n")
                        continue
                    
                    # 识别小节标题
                    if re.match(r'^\d+[\.\、]', line) and len(line) < 50:
                        markdown_content.append(f"\n### {line}\n")
                        continue
                    
                    # 识别更小节标题
                    if re.match(r'^\d+\.\d+', line) and len(line) < 50:
                        markdown_content.append(f"\n#### {line}\n")
                        continue
                    
                    # 识别摘要、关键词等特殊部分
                    if line in ['摘要', 'Abstract', '关键词', 'Keywords']:
                        markdown_content.append(f"\n## {line}\n")
                        continue
                    
                    # 处理普通段落
                    markdown_content.append(f"{line}\n")
                
                # 添加分页标记
                if page_num < total_pages:
                    markdown_content.append(f"\n---\n**第 {page_num} 页**\n\n")
    
    # 写入Markdown文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(markdown_content))
    
    print(f"\n✅ 转换完成！")
    print(f"📄 输出文件：{output_path}")
    print(f"📊 总页数：{total_pages}")

if __name__ == "__main__":
    import glob
    
    # 使用glob查找PDF文件
    pdf_files = glob.glob("/Users/kmduyy/Desktop/tianyuan/paper/*.pdf")
    
    if not pdf_files:
        print("❌ 未找到PDF文件")
        exit(1)
    
    pdf_path = pdf_files[0]
    print(f"找到PDF文件：{pdf_path}")
    
    output_path = "/Users/kmduyy/Desktop/tianyuan/paper/类脑AGI架构天元系统.md"
    
    extract_pdf_to_markdown(pdf_path, output_path)
