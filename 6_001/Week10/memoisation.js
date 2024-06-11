function memoise(fn) {
    let cache = {};
    return function (...args) {
        if (cache[args])
            return cache[args];

        const res = fn.apply(this, args);
        cache[args] = res;
        return res;
    }
}

function fib(n) {
    if (n < 2)
        return n;
    else
        return fib(n - 1) + fib(n - 2);

}

let f = memoise(fib);
console.log(f(40));

function fib1(n) {
    if (n < 2)
        return n;
    let a = 0, b = 1;
    for (let i = 1; i < n; i++) {

        b += a;
        a = b - a;
    }
    return b;
}

function memoisedFib(fn) {
    let cache = {};
    return function (...args) {
        if (cache[args])
            return cache[args];
        const res = fn.apply(this, args);
        cache[args] = res;
        return res;
    }

}

const f1 = memoisedFib((n) => fib(n));
console.log(f1(10));