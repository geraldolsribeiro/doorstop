# 1.0 Automated Tests

## 1.1 LLT001

Test adding items:

> `doorstop/core/test/test_document.py` (line 258)

*Parent links: REQ003*

## 1.2 LLT002

Test publishing Markdown:

> `doorstop/core/test/test_all.py` (line 612)

*Parent links: REQ004*

## 1.3 LLT003

Test publishing text:

> `doorstop/core/test/test_all.py` (line 587)

*Parent links: REQ007*

## 1.4 LLT004

Test getting items from a document:

> `doorstop/core/test/test_document.py` (line 140)

*Parent links: REQ008*

## 1.5 LLT005

Test referencing an external file by name:

> `doorstop/core/test/test_item.py` (line 454)

*Parent links: REQ001*

# 2.0 Inspection Tests

## 2.1 LLT007

These checks ensure the version control system (VCS) meets the needs of requirements management:

- Verify the VCS includes a 'tag' feature.
- Verify the VCS stores files in a permanent and secure manner.
- Verify the VCS handles change management of files.
- Verify the VCS associates changes to existing developer acccounts.
- Verify the VCS can manage changes to thousands of files.

*Parent links: REQ009, REQ011, REQ012, REQ013, REQ014, REQ015*

## 2.2 LLT008

These checks ensure the Python package is distributed properly:

- Verify the installation can be performed on a new computer in fewer than 10 seconds.

*Parent links: REQ015*
