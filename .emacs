(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes '(tango-dark))
 '(global-display-line-numbers-mode t)
 '(package-selected-packages '(treemacs lsp-mode ivy projectile magit popwin))
 '(tool-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "Consolas" :foundry "outline" :slant normal :weight regular :height 181 :width normal)))))
(global-display-line-numbers-mode)
(require 'package)
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)
;; Projectile mode activation
(projectile-mode +1)

;; Neotree setup and automatic opening
;; (require 'neotree)
;; (global-set-key [f8] 'neotree-toggle)
;; (add-hook 'emacs-startup-hook 'neotree-toggle)

;; Treemacs setup and automatic opening
(require 'treemacs)
(add-hook 'emacs-startup-hook 'treemacs)
(setq treemacs-position 'right)
(global-set-key (kbd "M-q") 'treemacs)
