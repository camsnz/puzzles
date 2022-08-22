import { jumpByIteration, jumpByRecursion } from "./jump"

const jumpBy = jumpByIteration; // jumpByRecursion;

describe("jump true examples", () => {
    it("edge cases", () => {
        expect(jumpBy([])).toEqual(true)
        expect(jumpBy([0])).toEqual(true)
        expect(jumpBy([1])).toEqual(true)
        expect(jumpBy([-1])).toEqual(true)
    })
    it("example case", () => {
        expect(jumpBy([2,3,1,1,4])).toEqual(true)
    })
    it("extra cases", () => {
        expect(jumpBy([1,0])).toEqual(true)
        expect(jumpBy([1,1,1,1])).toEqual(true)
        expect(jumpBy([1,1,1,0])).toEqual(true)
        expect(jumpBy([4,0,0,0,0])).toEqual(true)
        expect(jumpBy([3,0,0,3,0,0,0])).toEqual(true)
    })
    it("complex cases", () => {
        expect(jumpBy([3,3,0,0,1,0])).toEqual(true)
    })
})

describe("jump false examples", () => {
    it("edge cases", () => {
        expect(jumpBy([-100,1])).toEqual(false)
        expect(jumpBy([-1,1])).toEqual(false)
        expect(jumpBy([0,1])).toEqual(false)
        expect(jumpBy([1,0,1])).toEqual(false)
    })
    it("example case", () => {
        expect(jumpBy([3,2,1,0,4])).toEqual(false)
    })
    it("extra cases", () => {
        expect(jumpBy([1,1,1,0,1])).toEqual(false)
        expect(jumpBy([4,0,0,0,0,1])).toEqual(false)
        expect(jumpBy([3,0,0,3,0,0,0,1])).toEqual(false)
    })
})