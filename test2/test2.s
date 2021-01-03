.section .text
.globl _start
flag:
    .ascii "Change_me_pls"

_start:
    xorq %rdx, %rdx
    xorq %rdi, %rdi

    movq $flag, %rax
    
    movb $'V', %dl
    xorb (%rax), %dl
    orb %dl, %dil

    movb $'3', %dl
    xorb 1(%rax), %dl
    orb %dl, %dil

    movb $'r', %dl
    xorb 2(%rax), %dl
    orb %dl, %dil

    movb $'y', %dl
    xorb 3(%rax), %dl
    orb %dl, %dil

    movb $'_', %dl
    xorb 4(%rax), %dl
    orb %dl, %dil

    movb $'g', %dl
    xorb 5(%rax), %dl
    orb %dl, %dil

    movb $'0', %dl
    xorb 6(%rax), %dl
    orb %dl, %dil

    movb $'0', %dl
    xorb 7(%rax), %dl
    orb %dl, %dil

    movb $'d', %dl
    xorb 8(%rax), %dl
    orb %dl, %dil

    movb $'_', %dl
    xorb 9(%rax), %dl
    orb %dl, %dil

    movb $'s', %dl
    xorb 10(%rax), %dl
    orb %dl, %dil

    movb $'1', %dl
    xorb 11(%rax), %dl
    orb %dl, %dil

    movb $'r', %dl
    xorb 12(%rax), %dl
    orb %dl, %dil

    movq $0x3c, %rax
    syscall
    
