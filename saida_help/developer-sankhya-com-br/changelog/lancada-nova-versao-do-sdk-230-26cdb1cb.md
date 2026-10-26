---
id: "https://developer.sankhya.com.br/changelog/lançada-nova-versão-do-sdk-230"
titulo: "Lançada nova versão do SDK (2.3.0)"
url: "https://developer.sankhya.com.br/changelog/lançada-nova-versão-do-sdk-230"
---

# Lançada nova versão do SDK (2.3.0)

Add-on Studio 2.3.0 traz logs remotos, validação de group no Gradle, correções no compilador e um breaking change: a flag accessControlled em @ActionButton foi depreciada e causa falhas de compilação

## 🚀 Novas Funcionalidades

* **Logs Remotos**\
  Envio de logs para um serviço centralizado, facilitando o debug e permitindo ações proativas sobre erros.\
  **Obs.:** requer configuração correta do endpoint.
* **Validação do `group` no Gradle raiz**\
  Grupos da Sankhya são bloqueados quando os logs remotos estão habilitados.\
  **Impacto:** builds podem falhar caso o `group` não esteja conforme.

***

## ⚠️ Breaking Change

* A flag **`accessControlled`** foi **depreciada** na anotação `@ActionButton`.
* Projetos que ainda utilizam `accessControlled = true` **vão falhar na compilação**.

***

## 🛠️ Correções

* Compilador de dashboards corrigido.
* Correções na compilação de projetos somente Kotlin.
