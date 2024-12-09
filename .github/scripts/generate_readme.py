import os
import json
import random
from datetime import datetime

def generate_personal_flex():
    user_info = json.loads(os.environ['USER_INFO'])
    username = user_info['username']
    languages = json.loads(user_info['languages'])
    contributions = user_info['contributions']

    # Generate personalized vim tricks based on user's top languages
    vim_tricks = []
    for lang in languages:
        if lang.lower() == 'python':
            vim_tricks.append('`:py3do` for Python list comprehensions')
        elif lang.lower() == 'javascript':
            vim_tricks.append('`gqq` for formatting JSX')
        elif lang.lower() == 'rust':
            vim_tricks.append('`rust-analyzer` integration shortcuts')
        # Add more language-specific tricks

    # Generate README content
    readme = f"""# {username}'s Dev Environment Flex 🚀

> Automatically generated based on your GitHub profile's tech stack!

## Your Tech Signature

```vim
" Your Most Used Languages
{chr(10).join([f'let g:expertise_{i} = "{lang}"' for i, lang in enumerate(languages, 1)])}

" Your Contribution Power Level
let g:power_level = {contributions}
```

## Personal Vim Tricks

Based on your tech stack, here are some power moves:

{chr(10).join([f'- {trick}' for trick in vim_tricks])}

## Your Generated Scenes

Check out your personalized terminal recordings in `/asciinema`:
- `scene-1.cast`: Your dev environment setup
- `scene-2.cast`: Your language-specific tricks
- `scene-3.cast`: Your debugging flow

## Your Stats Visualization

![Your Dev Stats](./stats/dev_radar.svg)

## Share Your Flex!

Show off your automated dev environment by sharing:
```bash
curl -L https://github.com/{username}/vim-iphone-shorts-video-props/asciinema/scene-1.cast | asciinema play -
```

_Generated on {datetime.now().strftime('%Y-%m-%d')} based on your GitHub profile_
"""
    
    with open('README.md', 'w') as f:
        f.write(readme)

if __name__ == '__main__':
    generate_personal_flex()