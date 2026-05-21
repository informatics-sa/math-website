# Saudi Math Team Website
This website is made by the students on the Saudi Team, to preserve history of Saudi Math Team in one place.

This website includes: olympiads, participations, members, and exams.

## Documentation
Read [Website public data files](https://sainformatics.org/data/) documentation.

You might also refer to [Developer documentation](https://sainformatics.org/data/dev).

## Local Build
### Prerequisites
You need:
- [Python Interpreter](https://python.org)
- [Ruby Interpreter](https://www.ruby-lang.org)
- Install Ruby dependencies using [Bundler](https://bundler.io):
```sh
bundle install
```

<details>
    <summary>How does it work?</summary>
    `bundle` is a package manager, `Gemfile` contains the packages list.
    Jekyll latest version is 4.4.1, but the current version used in Github pages is 
</details>

### Building & Local Serving
```sh
python build.py && bundle exec jekyll serve -s ./root
```

## Maintainers
This website needs people who maintain the data up-to-date.

Current maintainers:
- Muaath Alqarni
- Mohammed Shaiban
- Ali Alsalman
- Yusuf Alkhalawi

## License
This project is licensed under the GNU General Public License v3.0.

Check [LICENSE](https://github.com/informatics-sa/informatics-sa.github.io/blob/main/LICENSE)
