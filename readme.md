# Домашнее задание по REST HTTP

На третьем семинаре по HTTP мы разобрали примеры RESTful API. В качестве простого небольшого упражнения предлагается спроектировать и написать свой маленький REST на любом HTTP фреймворке с тестами.

## Что хотим получить?

В третьем семинаре был пример RESTful HTTP API для `article`. Вам предлагается придумать любую сущность и спроектировать HTTP интерфейс для создания сущностей, получения полного списка (фильтры не нужны), удаления и изменения отдельных сущностей. Для реализации сервера можно выбрать любой популярный язык и любой удобный фреймворк, в примере лежит hello-world-пример из Flask. Тесты необходимо написать с помощью прямых HTTP запросов к серверу с помощью библиотеки `requests`.

Задание считается выполненым, если
1. написана простая описывающая документация на доступные endpoint'ы,
2. сервер поднимается на 80 порту в контейнере server (о шаблоне ниже)
3. на каждый endpoint написан хотя бы один тест и он зелёный

## Описание шаблона

Этот репозиторий предлагается форкнуть на GitLab, так как у него есть бесплатный CI для приватных репозиториев. Пайплайн CI описан в файле `.gitlab-ci.yml`, но вам его трогать не надо. Пайплайн собирает контейнеры с сервером и тестами и запускает тесты. Наличие документации он не проверяет, её предлагается положить где-нибудь внутри `src`, можно в `src/README.md`.

В `src` есть две папки:
  - `server`, папка с вашим сервером, содержащая любой код и Dockerfile
  - `client`, папка с тестами на pytest и Dockerfile

> TODO: Как запустить шаблон без докера
> TODO: Как запустить шаблон в докере