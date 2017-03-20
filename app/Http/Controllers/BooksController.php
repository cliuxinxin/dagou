<?php

namespace App\Http\Controllers;

use App\Book;
use Auth;
use Illuminate\Http\Request;

class BooksController extends Controller
{
    /**
     * Only user can add a book
     */
    public function __construct()
    {

        $this->middleware('auth')->only(['store']);
    }

    /**
     *
     * Show all the books
     *
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */
    public function index()
    {
        $items = Book::with('user')->paginate(20);

        return view('books.index',compact('items'));
    }

    /**
     * User create a book
     */
    public function store()
    {
        Auth::user()->books()->create(request(['name','detail']));

        return back();

    }
}
