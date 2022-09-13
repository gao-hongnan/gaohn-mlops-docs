## Customize Terminal

!!! Tip
    See Eric's zsh for better customization.

- Customize your terminal: [Oh My ZSH + Powerlevel10k](https://www.swtestacademy.com/customize-mac-terminal/).

- The default settings put the virtual environments like conda or virtualenv to the right without parenthesis;
  we can change this by the following [steps](https://github.com/romkatv/powerlevel10k/issues/780):
  
  - Open the settings of Powerlevel10k by calling code ~/.p10k.zsh;
  
  - To display conda environment with parentheses, find POWERLEVEL9K_ANACONDA_CONTENT_EXPANSION and change it like this:
  
  
zsh
  typeset -g POWERLEVEL9K_ANACONDA_CONTENT_EXPANSION='${CONDA_PROMPT_MODIFIER% }'
  
  
  This can be applied to other types of virtual environments as well.

  - To place the prompt to the left, just copy the ones you want from POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS
    to POWERLEVEL9K_LEFT_PROMPT_ELEMENTS.

## VSCode Extensions and Settings

