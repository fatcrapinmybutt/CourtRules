#!/usr/bin/env python3
"""
Split large markdown files in CourtRules repository for better performance.
This script identifies and splits files larger than the target size.
"""

import re
import os
from pathlib import Path
from datetime import datetime, timezone


def clean_filename(text):
    """Clean text for use in filename (remove special characters)."""
    # Remove special characters but keep alphanumeric, spaces, hyphens, underscores
    clean = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces and hyphens with underscores
    clean = clean.replace(' ', '_').replace('-', '_')
    # Normalize multiple underscores to single
    clean = re.sub(r'_+', '_', clean)
    # Remove leading/trailing underscores
    clean = clean.strip('_')
    # Limit length
    if len(clean) > 100:
        clean = clean[:100]
    return clean


def split_markdown_file(file_path, target_lines=500):
    """Split a markdown file into smaller files based on heading hierarchy."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # If file is already small enough, return
    if len(lines) <= target_lines:
        print(f"File {file_path.name} is already small enough ({len(lines)} lines)")
        return [file_path]
    
    # Find all top-level headings (## Heading)
    sections = []
    current_section = []
    current_heading = None
    
    for line in lines:
        if line.startswith('## '):
            # Save previous section
            if current_heading:
                sections.append((current_heading, current_section))
            
            # Start new section
            current_heading = line
            current_section = [line]
        else:
            if current_heading:
                current_section.append(line)
    
    # Save last section
    if current_heading:
        sections.append((current_heading, current_section))
    
    # If we have sections, split them
    if len(sections) > 1:
        print(f"Splitting {file_path.name} ({len(lines)} lines) into {len(sections)} sections")
        
        # Create output directory
        output_dir = file_path.parent / f"{file_path.stem}_split"
        output_dir.mkdir(exist_ok=True)
        
        # Write each section
        output_files = []
        for i, (heading, section_lines) in enumerate(sections):
            # Extract section number from heading if possible
            match = re.match(r'## (\d+)\.? (.*)', heading)
            if match:
                section_num = match.group(1)
                section_title = match.group(2)
            else:
                section_num = None
                section_title = heading[3:]
            
            # Clean heading for filename
            if section_num:
                clean_title = clean_filename(section_title)
                filename = f"{i+1:02d}_{section_num}_{clean_title}.md"
            else:
                clean_title = clean_filename(section_title)
                filename = f"{i+1:02d}_{clean_title}.md"
            
            # Ensure filename is valid and not too long
            if len(filename) > 200:
                filename = f"{i+1:02d}_section.md"
            
            output_file = output_dir / filename
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(section_lines))
            
            output_files.append(output_file)
            print(f"  Created {output_file.name} ({len(section_lines)} lines)")
        
        # Create index file
        index_content = f"""# {file_path.stem.capitalize().replace('-', ' ')} - Split Index

This directory contains the split version of `{file_path.name}`.

**Original File:** {file_path.name} ({len(lines)} lines, {len(content.encode('utf-8')):,} bytes)
**Split Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}
**Number of Sections:** {len(sections)}

## Sections

"""
        
        for i, (heading, section_lines) in enumerate(sections):
            output_file = output_dir / output_files[i].name
            # Clean heading for display
            display_heading = heading[3:] if heading.startswith('## ') else heading
            index_content += f"{i+1}. [{display_heading}](./{output_file.name}) - {len(section_lines)} lines\n"
        
        index_file = output_dir / "INDEX.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"  Created INDEX.md")
        
        return output_files + [index_file]
    else:
        print(f"File {file_path.name} has no clear sections to split")
        return [file_path]


def find_and_split_large_files(repo_path, min_lines=300):
    """Find and split all large markdown files in a repository."""
    repo_path = Path(repo_path)
    
    # Find all markdown files
    md_files = list(repo_path.rglob('*.md'))
    
    # Filter for large files
    large_files = []
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if len(lines) >= min_lines:
            large_files.append((md_file, len(lines)))
    
    # Sort by size (largest first)
    large_files.sort(key=lambda x: x[1], reverse=True)
    
    print(f"Found {len(large_files)} files with >= {min_lines} lines:")
    for md_file, line_count in large_files:
        print(f"  {md_file}: {line_count} lines")
    
    # Split each large file
    all_output_files = []
    for md_file, line_count in large_files:
        print(f"\nProcessing {md_file}...")
        output_files = split_markdown_file(md_file, min_lines)
        all_output_files.extend(output_files)
    
    return all_output_files


def create_optimization_directory(repo_path):
    """Create optimization directory structure."""
    repo_path = Path(repo_path)
    
    # Create optimization directory
    opt_dir = repo_path / 'optimization'
    opt_dir.mkdir(exist_ok=True)
    
    # Create README
    readme_content = f"""# CourtRules Optimization

This directory contains optimization scripts and resources for the CourtRules repository.

## Repository Statistics

- **Total Files:** {len(list(repo_path.rglob('*.md')))} markdown files
- **Large Files:** Files with >= 300 lines need splitting
- **Optimization Status:** Starting Phase 2

## Scripts

- `split_large_files.py` - Split large markdown files into smaller sections

## Optimization Plan

### Phase 2: Content Optimization
1. Split large files (>300 lines)
2. Create repository indexes
3. Standardize content formats
4. Create content templates

### Files to Split
- michigan-supreme-court-rules.md (799 lines)
- court-doc-processor/README.md (583 lines)
- michigan-court-of-appeals-rules.md (438 lines)
- litigating-higher-courts.md (383 lines)
- document-automation-guide.md (379 lines)
- federal-western-district-rules.md (356 lines)

## Usage

```bash
# Split all large files
python optimization/split_large_files.py .

# Split specific file
python optimization/split_large_files.py path/to/file.md
```

## Integration

This repository is part of the Ω-CONVERGENCE MICHIGAN LEGAL INTELLIGENCE SINGULARITY.
See [Michigan-MCLA/OPTIMIZATION_MASTER_PLAN.md](https://github.com/fatcrapinmybutt/Michigan-MCLA/blob/main/OPTIMIZATION_MASTER_PLAN.md) for the complete optimization roadmap.
"""
    
    with open(opt_dir / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"Created optimization directory: {opt_dir}")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python split_large_files.py <repository_path> [min_lines]")
        print("Default min_lines: 300")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    min_lines = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    
    print(f"=== Splitting Large Files in {repo_path} ===")
    print(f"Minimum lines to split: {min_lines}")
    
    # Create optimization directory
    create_optimization_directory(repo_path)
    
    # Find and split large files
    output_files = find_and_split_large_files(repo_path, min_lines)
    
    print(f"\n=== Summary ===")
    print(f"Processed {len(output_files)} files")
    print("Optimization complete!")
