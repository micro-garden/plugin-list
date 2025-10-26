# Micro Plugin List

This repository automatically collects and lists
[micro](https://micro-editor.github.io/) editor plugins.

You can browse the full plugin list here:  
**[micro Plugin List on GitHub Pages](https://micro-garden.github.io/plugin-list/)**

## How it works

- This project fetches GitHub repositories containing a `repo.json` file.
- The `repo.json` must be located in the root of the default branch
  (`main` or `master`).
- The file should contain an array of plugin metadata, each with `Name` and
  `Description` fields.

Example:

```json
[
  {
    "Name": "MyPlugin",
    "Description": "A plugin that does something useful"
  }
]
```

## License

The plugin list is generated from publicly available metadata.  
This repository itself is licensed under the MIT License.

## Author

Aki Kareha (aki@kareha.org)
