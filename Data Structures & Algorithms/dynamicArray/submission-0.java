class DynamicArray {
    Vector<Integer> vec;
    public DynamicArray(int capacity) {
        vec = new Vector<>(capacity);
    }

    public int get(int i) {
        return vec.get(i);
    }

    public void set(int i, int n) {
        vec.set(i,n);
    }

    public void pushback(int n) {
        vec.add(n);
    }

    public int popback() {
        return vec.remove(vec.size()-1);
    }

    private void resize() {
        vec.ensureCapacity(2*vec.capacity());
    }

    public int getSize() {
        return vec.size();
    }

    public int getCapacity() {
        return vec.capacity();
    }
}
