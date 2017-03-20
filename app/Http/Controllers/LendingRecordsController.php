<?php

namespace App\Http\Controllers;

use Auth;
use Carbon\Carbon;
use Illuminate\Http\Request;

class LendingRecordsController extends Controller
{
    /**
     * Only user can lend a book
     */
    public function __construct()
    {

        $this->middleware('auth')->only(['store']);
    }

    public function store($book)
    {
        Auth::user()->lendingbooks()->create([
            'book_id' => $book,
        ]);

        return back();
    }
}
