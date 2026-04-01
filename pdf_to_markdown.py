#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF转Markdown工具（论文排版优化版V2）
将学术论文PDF转换为Markdown格式，保持论文排版结构
"""

import pdfplumber
import re
import glob

def clean_text(text):
    """清理文本中的多余空白和特殊字符"""
    # 移除多余的空格
    text = re.sub(r' +', ' ', text)
    # 移除行首行尾空格
    text = text.strip()
    return text

def extract_pdf_to_markdown(pdf_path, output_path):
    """
    提取PDF内容并转换为Markdown格式（论文排版优化版V2）
    
    Args:
        pdf_path: PDF文件路径
        output_path: 输出Markdown文件路径
    """
    
    markdown_content = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"正在处理PDF文件，共 {total_pages} 页...")
        
        all_text = []
        
        # 先提取所有页面的文本
        for page_num, page in enumerate(pdf.pages, 1):
            print(f"处理第 {page_num}/{total_pages} 页...")
            text = page.extract_text()
            if text:
                all_text.append(text)
        
        # 合并所有文本
        full_text = '\n'.join(all_text)
        
        # 按行处理
        lines = full_text.split('\n')
        
        # 用于存储处理后的内容
        processed_lines = []
        
        i = 0
        title_found = False
        
        while i < len(lines):
            line = lines[i].strip()
            
            if not line:
                i += 1
                continue
            
            # 识别论文标题（只处理一次）
            if not title_found and '类脑AGI架构' in line and '天元' in line:
                # 合并标题的多行
                title_parts = [line]
                j = i + 1
                while j < len(lines) and j < i + 4:
                    next_line = lines[j].strip()
                    # 如果下一行是摘要或关键词，停止
                    if next_line.startswith('摘要') or next_line.startswith('关键词'):
                        break
                    # 如果下一行包含标题的关键部分，继续合并
                    if any(keyword in next_line for keyword in ['基于脉冲', '异构芯片', '全域机器', '河图洛书', '易经', '上古系统']):
                        title_parts.append(next_line)
                        j += 1
                    else:
                        break
                
                # 合并标题
                full_title = ''.join(title_parts)
                processed_lines.append(f"# {full_title}\n\n")
                title_found = True
                i = j
                continue
            
            # 识别英文标题
            elif line.startswith('TianYuan:') or 'TianYuan: A Brain-Inspired' in line:
                processed_lines.append(f"\n## {line}\n\n")
            
            # 识别摘要
            elif line == '摘要' or line == 'Abstract':
                processed_lines.append(f"\n## {line}\n\n")
            
            # 识别关键词
            elif line.startswith('关键词') or line.startswith('Keywords'):
                # 合并关键词的多行
                keyword_parts = [line]
                j = i + 1
                while j < len(lines) and j < i + 3:
                    next_line = lines[j].strip()
                    if next_line and not next_line.startswith('一、') and not next_line.startswith('1.'):
                        keyword_parts.append(next_line)
                        j += 1
                    else:
                        break
                full_keywords = ''.join(keyword_parts)
                processed_lines.append(f"\n### {full_keywords}\n\n")
                i = j
                continue
            
            # 识别一级标题（一、二、三等）
            elif re.match(r'^[一二三四五六七八九十]+、', line):
                processed_lines.append(f"\n## {line}\n\n")
            
            # 识别二级标题（1.1、1.2等）
            elif re.match(r'^\d+\.\d+\s', line) and len(line) < 80:
                processed_lines.append(f"\n### {line}\n\n")
            
            # 识别三级标题（1.1.1、1.1.2等）
            elif re.match(r'^\d+\.\d+\.\d+\s', line) and len(line) < 80:
                processed_lines.append(f"\n#### {line}\n\n")
            
            # 识别参考文献
            elif line.startswith('参考文献') or line.startswith('References'):
                processed_lines.append(f"\n## {line}\n\n")
            
            # 识别致谢
            elif line.startswith('致谢') or line.startswith('Acknowledgments'):
                processed_lines.append(f"\n## {line}\n\n")
            
            # 处理普通段落
            else:
                # 特殊处理：表格、图片等
                if re.match(r'^表\s*\d+', line):
                    processed_lines.append(f"\n**{line}**\n\n")
                elif re.match(r'^图\s*\d+', line):
                    processed_lines.append(f"\n**{line}**\n\n")
                elif re.match(r'^公式\s*\d+', line):
                    processed_lines.append(f"\n```\n{line}\n```\n\n")
                else:
                    # 普通文本，保持原样
                    processed_lines.append(f"{line}\n")
            
            i += 1
        
        # 写入Markdown文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(processed_lines))
        
        print(f"\n✅ 转换完成！")
        print(f"📄 输出文件：{output_path}")
        print(f"📊 总页数：{total_pages}")

if __name__ == "__main__":
    # 使用glob查找PDF文件
    pdf_files = glob.glob("/Users/kmduyy/Desktop/tianyuan/paper/*.pdf")
    
    if not pdf_files:
        print("❌ 未找到PDF文件")
        exit(1)
    
    pdf_path = pdf_files[0]
    print(f"找到PDF文件：{pdf_path}")
    
    output_path = "/Users/kmduyy/Desktop/tianyuan/paper/类脑AGI架构天元系统.md"
    
    extract_pdf_to_markdown(pdf_path, output_path)
