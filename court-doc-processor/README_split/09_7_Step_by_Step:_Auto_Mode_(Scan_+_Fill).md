## 7. Step-by-Step: Auto Mode (Scan + Fill)

### When to Use

Use the `auto` command for the most streamlined workflow: provide a source document and a target template in one command.

### Command Syntax

```bash
python processor.py auto <SOURCE_FILE> <TEMPLATE_KEY> [OPTIONS]
```

### Step-by-Step Procedure

```bash
# Example: Received a complaint, need to draft an answer

# Step 1: Auto-extract and fill the answer template
python processor.py auto \
    received_complaint.pdf \
    michigan/circuit/civil/answer \
    --prompt \
    -o draft_answer.txt

# Example: Have a prior divorce judgment, need to file a custody modification
python processor.py auto \
    existing_judgment.pdf \
    michigan/circuit/domestic-relations/motion-custody \
    --prompt \
    -o motion_custody_draft.txt
```

**Step 1:** Run the auto command with `--prompt` so you are asked for any fields not extracted.

**Step 2:** Answer each prompt. Press Enter to skip (field will be marked `<<<...>>>`).

**Step 3:** Review the output file.

**Step 4:** Edit remaining `<<<FIELD_NAME>>>` markers in your text editor.

**Step 5:** Have the document reviewed by a licensed attorney before filing.

---
