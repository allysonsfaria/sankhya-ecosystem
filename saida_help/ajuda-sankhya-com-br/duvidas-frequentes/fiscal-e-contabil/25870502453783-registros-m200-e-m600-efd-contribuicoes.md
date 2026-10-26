---
id: "25870502453783"
titulo: "Registros M200 e M600 - EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25870502453783-Registros-M200-e-M600-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-10-16T20:30:15Z"
rotulos: ["Configuração", "Relatórios", "Fiscal", "Impostos", "EFD Contribuições", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Registros M200 e M600"]
---

# Registros M200 e M600 - EFD Contribuições

O sistema Sankhya não realiza a geração dos registros M200 e M600 no arquivo da EFD-Contribuições. Esses registros correspondem à consolidação da apuração do PIS/Pasep e da Cofins, respectivamente, e são gerados por meio da funcionalidade **Gerar Apuração das Contribuições**, disponível no PVA da EFD-Contribuições.

Embora o Sankhya permita a geração desses registros pela tela HTML5, eles são apresentados com valores zerados, desde que atendidas determinadas condições de configuração. Uma das condições envolve uma variável que pode impedir sua geração automática. Além disso, quando existem valores construídos automaticamente nos registros M410 e M810, os registros M200 e M600 não são gerados pelo sistema.

Dessa forma, a apuração dos valores dos registros M200 e M600 deve ser realizada no próprio PVA, por meio da funcionalidade de geração da apuração das contribuições, que consolida as informações escrituradas no arquivo e calcula os valores correspondentes, conforme as regras aplicáveis.
