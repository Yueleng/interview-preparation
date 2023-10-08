// 记录Promise的三种状态
const PENDING = "pending";
const FULFILLED = "fulfilled";
const REJECTED = "rejected";

/**
 * Run a task in micro task queue
 * pass a callback func into it
 * @param {*} callback
 */
function runMicroTask(callback) {
  // determine node env
  // to avoid `undefined` error, using globalThis
  // globalThis is a global variable
  // in Browser, it refers to window
  // in node, it refers to global
  if (globalThis.process && globalThis.process.nextTick) {
    globalThis.process.nextTick(callback);
  } else if (globalThis.MutationObserver) {
    const p = document.createElement("p");
    const observer = new MutationObserver(callback);
    observer.observe(p, {
      childList: true,
    });
    p.innerHTML("1");
  } else {
    setTimeout(callback, 0);
  }
}

/**
 * determine if an object is Promise
 */
function isPromise(obj) {
  return !!(obj && typeof obj === "object" && typeof obj.then === "function");
}

class MyPromise {
  /**
   *
   * @param {*} executor
   * execute synchronously
   */
  constructor(executor) {
    this._state = PENDING;
    this._value = undefined;
    this._handlers = [];
    try {
      executor(this._resolve.bind(this), this._reject.bind(this));
    } catch (error) {
      this._reject(error);
      console.error(error);
    }
  }

  /**
   *
   * @param {Function} executor
   * @param {String} state in what circumstances this executor will execute
   * @param {Function} resolve
   * @param {Function} reject
   */
  _pushHandlers(executor, state, resolve, reject) {
    this._handlers.push({
      executor,
      state,
      resolve,
      reject,
    });
  }

  _runHandlers() {
    if (this._state === PENDING) {
      return;
    }

    while (this._handlers[0]) {
      const handler = this._handlers[0];
      this._runOneHandler(handler);
      this._handlers.shift();
    }
  }

  _runOneHandler({ executor, state, resolve, reject }) {
    runMicroTask(() => {
      if (this._state !== state) {
        return;
      }

      if (typeof executor !== "function") {
        this._state === FULFILLED ? resolve(this._value) : reject(this._value);
        return;
      }
      try {
        const result = executor(this._value);
        if (isPromise(result)) {
          result.then(resolve, reject);
        } else {
          resolve(result);
        }
      } catch (error) {
        reject(error);
        console.error(error);
      }
    });
  }

  then(onFulfilled, onRejected) {
    return new MyPromise((resolve, reject) => {
      this._pushHandlers(onFulfilled, FULFILLED, resolve, reject);
      this._pushHandlers(onRejected, REJECTED, resolve, reject);
      this._runHandlers();
    });
  }

  catch(onRejected) {
    return this.then(null, onRejected);
  }

  finally(onSettled) {
    return this.then(
      (data) => {
        onSettled();
        return data;
      },
      (reason) => {
        onSettled();
        throw reason;
      }
    );
  }

  _changeState(newState, value) {
    if (this._state !== PENDING) {
      return;
    }

    if (isPromise(value)) {
      value.then(this._resolve.bind(this), this._reject.bind(this));
      return;
    }

    this._state = newState;
    this._value = value;
    this._runHandlers();
  }

  _resolve(data) {
    this._changeState(FULFILLED, data);
  }

  _reject(reason) {
    this._changeState(REJECTED, reason);
  }

  static resolve(data) {
    if (data instanceof MyPromise) {
      return data;
    }
    return new MyPromise((resolve, reject) => {
      if (isPromise(data)) {
        data.then(resolve, reject);
      } else {
        resolve(data);
      }
    });
  }

  /**
   * 得到一个被拒绝的Promise
   * @param {any}} reason
   */
  static reject(reason) {
    return new MyPromise((resolve, reject) => {
      reject(reason);
    });
  }

  /**
   * 得到一个新的Promise
   * 该Promise的状态取决于proms的执行
   * proms是一个迭代器，包含多个Promise
   * 全部Promise成功，则返回的Promise成功，数据为所有Promise成功的数据，并且顺序是按照传入的顺序排列
   * 只要有一个Promise失败，则返回的Promise失败，原因是第一个失败的Promise的原因
   * @param {iterator} proms
   */
  static all(proms) {
    return new MyPromise((resolve, reject) => {
      try {
        const results = [];
        let count = 0; // Promise的总数
        let fulfilledCount = 0; // 已完成的数量
        for (const p of proms) {
          let i = count;
          count++;
          MyPromise.resolve(p).then((data) => {
            fulfilledCount++;
            results[i] = data;
            if (fulfilledCount === count) {
              // 当前是最后一个Promise完成了
              resolve(results);
            }
          }, reject);
        }
        if (count === 0) {
          resolve(results);
        }
      } catch (error) {
        reject(error);
        console.error(error);
      }
    });
  }

  /**
   * 等待所有的Promise有结果之后
   * 该方法返回的Promise完成
   * 并且按照顺序将所有结果汇总
   * @param {iterator} proms
   */
  static allSettled(proms) {
    const ps = [];
    for (const p of proms) {
      ps.push(
        MyPromise.resolve(p).then(
          (value) => ({
            status: FULFILLED,
            value,
          }),
          (reason) => ({
            status: REJECTED,
            reason,
          })
        )
      );
    }
    return MyPromise.all(ps);
  }

  /**
   * 返回的Promise与第一个有结果的一致
   * @param {iterator} proms
   */
  static race(proms) {
    return new MyPromise((resolve, reject) => {
      for (const p of proms) {
        MyPromise.resolve(p).then(resolve, reject);
      }
    });
  }
}

const promise = new MyPromise((resolve, reject) => {
  resolve(123);
});

console.log(promise);
