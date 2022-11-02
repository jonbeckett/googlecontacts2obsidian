# contacts2obsidian

I wrote this script largely for my own purposes, but thought the community might find use for it too. The script reads an exported Google Contacts CSV file, and turns it into markdown files suitable for placing in a Obsidian vault - complete with YAML in case you're using the dataview plugin, or something similar.

Example Usage:

`> python contacts2obsidian.py c:\contacts.csv c:\Vault\Resources\Contacts

A few notes:

- phone numbers and email addresses are turned into an array in the YAML, but are listed in the formatted content
- each contact is suffixed with the tag #contact