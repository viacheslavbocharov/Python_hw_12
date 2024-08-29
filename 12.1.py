import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
          html = file.read()
          clean_text = re.sub(r'<[^>]+>', '', html)
          clean_lines = [line for line in clean_text.splitlines() if line.strip()]
          cleaned_text_without_empty_lines = "\n".join(clean_lines)

      with codecs.open(result_file, 'w', 'utf-8') as output_file:
          output_file.write(cleaned_text_without_empty_lines)


delete_html_tags('draft.html')